# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.views.generic import ListView, DetailView
from django.views.generic.list import MultipleObjectMixin
from django.utils.translation import gettext as _

from library.logic import filter_items
from .models import Category
from book.models import Book


class Index(ListView):
    model = Category
    template_name = 'category/index.html'
    context_object_name = 'latest_category_list'
    paginate_by = settings.PAGE_LIST_AMOUNT_CAT

    def get_queryset(self):
        return Category.objects.order_by('pub_date')

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)

        context.update({
            'section_title': _('Категорії'),
            'url_part': 'category:detail',
        })

        return context


class Detail(DetailView, MultipleObjectMixin):
    model = Category
    template_name = 'category/detail.html'
    context_object_name = 'category'
    paginate_by = settings.PAGE_LIST_AMOUNT_BOOK

    def get_context_data(self, **kwargs):
        category = kwargs['object']
        self.object_list = filter_items(Book).filter(category__slug=category.slug)

        context = super(Detail, self).get_context_data(**kwargs)

        return context
