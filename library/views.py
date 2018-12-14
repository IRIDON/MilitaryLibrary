from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import FormView
from django.conf import settings
from book.models import Book, Category, Author
from library.logic import filter_items
from .forms import ContactForm


class Index(TemplateView):
    template_name = 'library/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)

        context.update({
            'new_books': filter_items(Book, last=True)[:settings.ROW_ITEMS_AMOUNT],
            'most_views_books': filter_items(Book).order_by('hit_count_generic__hits').reverse()[:settings.ROW_ITEMS_AMOUNT],
        })
        return context


class Contact(FormView):
    template_name = 'library/forms/contact_form.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.send_email()

        return super(Contact, self).form_valid(form)

