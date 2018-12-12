# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


admin.site.register(Category, CategoryAdmin)
