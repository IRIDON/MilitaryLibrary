# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test import Client

from .models import Book, Author, Language


class BookSiteTests(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('book:index'))

        self.assertEqual(response.status_code, 200)
