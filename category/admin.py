# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import gettext as _
from django.contrib import admin
from django.utils.html import format_html
from django.core.urlresolvers import reverse

# Register your models here.
from .models import Category, Specialty

class ModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'page', 'pub_date']

    def page(self, object):
        url = reverse(self.url_part, kwargs={'slug': object.slug})

        return format_html(
            '<a href="{}" target="_blank">{}</a>',
            url,
            url
        )
    page.short_description = _('Перегляд')


class CategoryAdmin(ModelAdmin):
    url_part = 'category:detail'


class SpecialtyAdmin(ModelAdmin):
    url_part = 'specialty:detail'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Specialty, SpecialtyAdmin)
