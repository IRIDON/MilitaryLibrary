from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from library.logic import filter_items
from .models import Category, Specialty


class Map(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def lastmod(self, obj):
        return obj.pub_date


class CategorySitemap(Map):
    def items(self):
        return filter_items(Category).all()

    def location(self, Model):
        return reverse('category:detail', kwargs={'slug': Model.slug})


class SpecialtySitemap(Map):
    def items(self):
        return filter_items(Specialty).all()

    def location(self, Model):
        return reverse('specialty:detail', kwargs={'slug': Model.slug})

