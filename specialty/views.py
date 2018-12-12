# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Specialty
from book.models import Book


class IndexView(generic.ListView):
    template_name = 'specialty/index.html'
    context_object_name = 'latest_specialty_list'

    def get_queryset(self):
        return Specialty.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    template_name = 'specialty/detail.html'
    model = Specialty

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        specialty = context['specialty']

        context.update({
            'book_list': Book.objects.filter(specialty__slug=specialty.slug)
        })

        return context
