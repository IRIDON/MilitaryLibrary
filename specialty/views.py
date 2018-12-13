# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings
from django.views.generic import ListView, DetailView
from django.views.generic.list import MultipleObjectMixin

# Create your views here.
from django.views import generic
from .models import Specialty
from book.models import Book


class Index(ListView):
    model = Specialty
    template_name = 'specialty/index.html'
    context_object_name = 'latest_specialty_list'
    paginate_by = settings.PAGE_LIST_AMOUNT_CAT

    def get_queryset(self):
        return Specialty.objects.order_by('-pub_date')


class Detail(DetailView, MultipleObjectMixin):
    model = Specialty
    template_name = 'specialty/detail.html'
    paginate_by = settings.PAGE_LIST_AMOUNT_BOOK

    def get_context_data(self, **kwargs):
        specialty = kwargs['object']
        self.object_list = Book.objects.order_by('-pub_date').filter(specialty__slug=specialty.slug)

        context = super(Detail, self).get_context_data(**kwargs)

        return context