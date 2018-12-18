# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import gettext as _
from django.contrib import admin
from django.utils.html import format_html
from django.core.urlresolvers import reverse

# Register your models here.
from .models import Book, Language


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'visible', 'page', 'view_category', 'view_specialty', 'pub_date']
    list_filter = ['pub_date', 'visible', 'category', 'specialty']
    fieldsets = [
        (None, {'fields': ['visible', 'name', 'slug', 'description', 'pub_date', 'author']}),
        ('Фаїли', {'fields': [('image', 'file'), 'file_url']}),
        ('Категорії', {'fields': [('category', 'specialty'), ('language')]}),
    ]

    def page(self, book):
		url = reverse('book:detail', kwargs={'slug': book.slug})

		return format_html(
			'<a href="{}" target="_blank">{}</a>',
			url,
			url
		)
    page.short_description = _('Перегляд')

    def view_category(self, book):
        return self.get_many_to_manu(book.category)
    view_category.short_description = _('Категорія')

    def view_specialty(self, book):
        return self.get_many_to_manu(book.specialty)
    view_specialty.short_description = _('Спеціальність')

    def get_many_to_manu(self, object):
        result = []

        for val in object.values():
            result.append(val['name'])

        return result



class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'iso']


admin.site.register(Book, BookAdmin)
admin.site.register(Language, LanguageAdmin)
