from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import FormView
from django.conf import settings

from django.shortcuts import render
from simple_search import search_filter

from book.models import Book, Category
from library.logic import filter_items
from .forms import ContactForm


class Index(TemplateView):
    template_name = 'library/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)

        context.update({
            'new_books': filter_items(Book, last=True)[:settings.ROW_ITEMS_AMOUNT],
            'most_views_books': filter_items(Book).order_by('hit_count_generic__hits')[:settings.ROW_ITEMS_AMOUNT],
        })

        return context


class Contact(FormView):
    template_name = 'library/forms/contact_form.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.send_email()

        return super(Contact, self).form_valid(form)


class Search(TemplateView):
    template_name = 'library/search.html'

    def get(self, request, **kwargs):
        data = request.GET.dict()
        keyword = data['search'].lower()
        search_fields = ['name', 'description', 'author']

        context = {
            'keyword': keyword,
        }

        if len(keyword) >= settings.SEARCH_MIN_LENGHT:
            search = filter_items(Book).filter(search_filter(search_fields, keyword))

            context.update({
                'search_list': search,
            })
        else:
            context.update({
                'keyword_error': settings.SEARCH_MIN_LENGHT,
            })

        return super(TemplateView, self).render_to_response(context)
