from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from library.logic import filter_items

class StaticViewSitemap(Sitemap):
    priority = 1
    changefreq = 'daily'

    def items(self):
        return ['index', 'category:index', 'specialty:index', 'contact-us']

    def location(self, item):
        return reverse(item)
