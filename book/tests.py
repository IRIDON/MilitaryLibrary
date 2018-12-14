# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.utils import timezone

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test import Client

from .models import Book, Author, Language


def create_book(visible, name, time):
    time_now = timezone.now()
    time_past = time_now - datetime.timedelta(days=7)

    return Book.objects.create(
        visible=visible,
        name=name,
        pub_date= time_now if time == 'now' else time_past
    )


class BookSiteTests(TestCase):
    def setUp(self):
        create_book(True, 'Test book name 1', 'now')
        create_book(False, 'Test book name 2', 'now')
        create_book(False, 'Test book name 3', 'past')
        create_book(True, 'Test book name 4', 'past')
        create_book(True, 'Test book name 5', 'past')
        create_book(True, 'Test book name 6', 'past')
        create_book(True, 'Test book name 7', 'now')
        create_book(True, 'Test book name 8', 'now')

    def test_index_page(self):
        response = self.client.get(reverse('book:index'))
        print(Book.objects.get(id=1))
        print(dir(response))

        print(response.context)
        self.assertEqual(response.status_code, 200)
