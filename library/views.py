from django.views.generic import TemplateView
from book.models import Book, Category, Author

ITEMS_AMOUNT = 3

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        book = Book.objects.filter(visible=True)
    	
        context.update({
            'new_books': book.order_by('-pub_date')[:ITEMS_AMOUNT],
            'most_views_books': book.order_by('hit_count_generic__hits').reverse()[:ITEMS_AMOUNT],
        })
        return context