# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings
from django.views.generic import ListView, DetailView
from django.views.generic.list import MultipleObjectMixin
from django.utils.translation import gettext as _

# Create your views here.
from django.views import generic
from library.logic import filter_items
from .models import Specialty
from book.models import Book


class Index(ListView):
    model = Specialty
    template_name = 'category/index.html'
    context_object_name = 'latest_category_list'
    paginate_by = settings.PAGE_LIST_AMOUNT_CAT

    def get_queryset(self):
        return Specialty.objects.order_by('pub_date')

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)

        context.update({
            'section_title': _('Cпеціальності'),
            'url_part': 'specialty:detail',
        })

        return context


class Detail(DetailView, MultipleObjectMixin):
    model = Specialty
    template_name = 'category/detail.html'
    context_object_name = 'category'
    paginate_by = settings.PAGE_LIST_AMOUNT_BOOK

    def get_context_data(self, **kwargs):
        specialty = kwargs['object']
        self.object_list = filter_items(Book).filter(specialty__slug=specialty.slug)

        context = super(Detail, self).get_context_data(**kwargs)

        context.update({
            'section_title': _('Cпеціальності'),
            'url_part': 'specialty:detail',
        })

        return context