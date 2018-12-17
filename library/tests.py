import datetime

from django.utils import timezone
from django.test import Client
from django.test import TestCase
from django.core.urlresolvers import reverse

from book.models import Book, Author, Language

def create_book(visible, name, time):
    time_now = timezone.now()
    time_past = time_now - datetime.timedelta(days=7)

    return Book.objects.create(
        visible=visible,
        name=name,
        pub_date= time_now if time == 'now' else time_past
    )


new_books = [
    'Test book name 1',
    'Test book name 3',
    'Test book name 4'
]

class MainSiteTests(TestCase):
    def setUp(self):
        create_book(True, 'Test book name 1', 'now')
        create_book(False, 'Test book name 2', 'now')
        create_book(True, 'Test book name 3', 'now')
        create_book(True, 'Test book name 4', 'now')

        create_book(True, 'Test book name 5', 'past')
        create_book(False, 'Test book name 6', 'past')
        create_book(True, 'Test book name 7', 'past')
        create_book(True, 'Test book name 8', 'past')

    def test_index_page(self):
        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)

    def test_index_page_list_new_itrms(self):
        response = self.client.get(reverse('index'))

        for book in response.context['new_books']:
            self.assertEqual(new_books[::-1].index(book.name) != -1, True)

    def test_index_page_popular_itrms(self):
        response = self.client.get(reverse('index'))
        context = response.context['most_views_books']

        self.assertEqual(context.count(), 3)