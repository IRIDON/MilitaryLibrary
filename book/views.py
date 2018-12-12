# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import unicodedata

from django.shortcuts import render
from simple_search import search_filter

# Create your views here.
from django.views.generic import ListView, DetailView, TemplateView
from django.conf import settings
from hitcount.views import HitCountDetailView
from .models import Book


class IndexView(ListView):
    template_name = 'book/index.html'
    context_object_name = 'latest_book_list'

    def get_queryset(self):
        return Book.objects.filter(visible=True).all()


class Search(TemplateView):
    template_name = 'book/search.html'

    def get(self, request, **kwargs):
        data = request.GET.dict()
        keyword = data['search'].lower()
        search_fields = ['name', 'description']

        if len(keyword) >= settings.SEARCH_MIN_LENGHT:
            search = Book.objects.filter(visible=True).filter(search_filter(search_fields, keyword))

            context = {
                'search_list': search,
            }
        else:
            context = {
                'search_list': [],
                'keyword_error': settings.SEARCH_MIN_LENGHT,
            }

        return super(TemplateView, self).render_to_response(context)


class DetailView(HitCountDetailView):
    model = Book
    count_hit=True
    template_name = 'book/detail.html'

    def get_file_link(self, book):
        file = book.file

        if file:
            return file.url

        return book.file_url

    def get_file_type(self, link):
        available_files = ('pdf', 'txt', 'doc', 'djvu', 'fb2', 'epub', 'mobi', 'rtf', 'lrf')
        ext = re.search('\.[a-zA-Z0-9]+$', str(link))
        ext = ext.group(0).replace('.', '')
        ext = ext.encode('utf-8')

        if available_files.index(ext) != -1:
            return ext

        return None

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        file_link = self.get_file_link(context['book'])

        if file_link:
            context.update({
                'download_link': file_link,
                'download_file_type': self.get_file_type(file_link),
            })

        return context
