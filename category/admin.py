# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import gettext as _
from django.contrib import admin
from django.utils.html import format_html
from django.core.urlresolvers import reverse

# Register your models here.
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'page', 'pub_date']

    def page(self, object):
        url = reverse('category:detail', kwargs={'slug': object.slug})

        return format_html(
            '<a href="{}" target="_blank">{}</a>',
            url,
            url
        )
    page.short_description = _('Перегляд')


admin.site.register(Category, CategoryAdmin)
