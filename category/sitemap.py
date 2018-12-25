from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from library.logic import filter_items
from .models import Category, Specialty


class CategorySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return filter_items(Category).all()

    def location(self, Model):
        return reverse('category:detail', kwargs={'slug': Model.slug})

    def lastmod(self, obj):
        return obj.pub_date

class SpecialtySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return filter_items(Specialty).all()

    def location(self, Model):
        return reverse('specialty:detail', kwargs={'slug': Model.slug})

    def lastmod(self, obj):
        return obj.pub_date
