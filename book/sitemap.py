from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from library.logic import filter_items
from .models import Book

class BookSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.5

    def items(self):
        return filter_items(Book).all()

    def location(self, Model):
        return reverse('book:detail', kwargs={'slug': Model.slug})

    def lastmod(self, obj):
        return obj.pub_date
