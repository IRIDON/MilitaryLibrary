# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404

# Create your views here.
from django.views import generic
from .models import Category
from book.models import Book


class IndexView(generic.ListView):
    template_name = 'category/index.html'
    context_object_name = 'latest_category_list'

    def get_queryset(self):
        return Category.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    template_name = 'category/detail.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        category = context['category']

        context.update({
            'book_list': Book.objects.filter(category__slug=category.slug)
        })

        return context
