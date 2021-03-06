# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import reverse


class CategorySiteTests(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('category:index'))

        self.assertEqual(response.status_code, 200)
