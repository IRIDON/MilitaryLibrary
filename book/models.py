# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import gettext as _
from django.contrib.contenttypes.fields import GenericRelation
from specialty.models import Specialty
from category.models import Category

from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField

from hitcount.models import HitCount, HitCountMixin
from tinymce.models import HTMLField


class Language(models.Model):
    name = models.CharField(
        unique=False,
        blank=False,
        max_length=100,
        verbose_name=_('Назва')
    )
    iso = models.CharField(
        unique=True,
        blank=False,
        max_length=2,
        verbose_name=_('ISO країни')
    )

    class Meta:
        verbose_name = _('Мову')
        verbose_name_plural = _('Мови')

    def __unicode__(self):
        return "%s" % self.name


class Book(models.Model, HitCountMixin):
    visible = models.BooleanField(
        default=True,
        verbose_name=_('Показувати')
    )
    name = models.CharField(
        blank=False, 
        null=True, 
        max_length=100,
        verbose_name=_('Назва')
    )
    pub_date = models.DateTimeField(
        blank=False,
        null=True,
        verbose_name=_('Дата публікації')
    )
    description = HTMLField(
        verbose_name=_('Опис')
    )
    file_url = models.URLField(
        blank=True, 
        null=True, 
        verbose_name=_('Посилання на файл')
    )
    file = FilerFileField(
        blank=True, 
        null=True, 
        related_name='download_file',
        verbose_name=_('Завантажити файл')
    )
    image = FilerImageField(
        blank=True, 
        null=True, 
        related_name="book_image"
    )
    author = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name=_('Автор')
    )
    language = models.ManyToManyField(
        Language,
        blank=True,
        verbose_name=_('Мова')
    )
    category = models.ManyToManyField(
        Category,
        blank=True,
        verbose_name=_('Категорія')
    )
    specialty = models.ManyToManyField(
        Specialty,
        blank=True,
        verbose_name=_('Спеціальність')
    )
    hit_count_generic = GenericRelation(
        HitCount, 
        object_id_field='object_pk',
        related_query_name='hit_count_generic_relation'
    )

    class Meta:
        verbose_name = _('Книгу')
        verbose_name_plural = _('Книги')

    def __unicode__(self):
        return "%s" % self.name



