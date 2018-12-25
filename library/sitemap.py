from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from library.logic import filter_items

class Map(Sitemap):
    changefreq = 'daily'

    def location(self, item):
        return reverse(item)


class MainPageSitemap(Map):
    priority = 1

    def items(self):
        return ['index']


class StaticSitemap(Map):
    priority = 0.7

    def items(self):
        return ['category:index', 'specialty:index', 'contact-us']
