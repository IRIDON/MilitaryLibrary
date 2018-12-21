# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import unicodedata

# Create your views here.
from django.views.generic import ListView, DetailView, TemplateView
from django.conf import settings
from hitcount.views import HitCountDetailView
from library.logic import filter_items, _get_file_type
from .models import Book


class Index(ListView):
    model = Book
    template_name = 'book/index.html'
    context_object_name = 'latest_book_list'
    paginate_by = settings.PAGE_LIST_AMOUNT_BOOK

    def get_queryset(self):
        return filter_items(Book).all()


class Detail(HitCountDetailView):
    model = Book
    count_hit = True
    template_name = 'book/detail.html'

    def get_file_link(self, book):
        file = book.file

        if file:
            return file.url

        return book.file_url

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)
        file_link = self.get_file_link(context['book'])

        if file_link:
            context.update({
                'download_link': file_link,
                'download_file_type': _get_file_type(file_link),
            })

        return context
