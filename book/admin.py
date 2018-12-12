# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.html import format_html
from django.core.urlresolvers import reverse

# Register your models here.
from .models import Book, Author, Language


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'visible', 'page', 'pub_date']

    def page(self, book):
		url = reverse('book:detail', kwargs={'pk': book.id})

		return format_html(
			'<a href="{}" target="_blank">{}</a>',
			url,
			url
		)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'iso']


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Language, LanguageAdmin)
