# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from specialty.models import Specialty
from category.models import Category

from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField

from hitcount.models import HitCount, HitCountMixin

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(
        unique=False,
        blank=False,
        null=True, 
        max_length=50,
        verbose_name=u"Ім'я:"
    )
    last_name = models.CharField(
        unique=False,
        blank=False,
        null=True, 
        max_length=50,
        verbose_name=u'Прізвище:'
    )
    patronymic = models.CharField(
        unique=False,
        blank=True,
        null=True, 
        max_length=50,
        verbose_name=u'По батькові:'
    )

    class Meta:
        verbose_name = u'Автор'
        verbose_name_plural = u'Автори'

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Language(models.Model):
    name = models.CharField(
        unique=False,
        blank=False,
        max_length=100,
        verbose_name=u'Назва:'
    )
    iso = models.CharField(
        unique=True,
        blank=False,
        max_length=2,
        verbose_name=u'ISO країни'
    )

    class Meta:
        verbose_name = u'Мова'
        verbose_name_plural = u'Мови'

    def __unicode__(self):
        return "%s" % self.name


class Book(models.Model, HitCountMixin):
    visible = models.BooleanField(
        default=True,
        verbose_name=u'Показувати:'
    )
    name = models.CharField(
        blank=False, 
        null=True, 
        max_length=100,
        verbose_name=u'Назва:'
    )
    pub_date = models.DateTimeField(
        blank=False,
        auto_now=True,
        null=True,
        verbose_name=u'Дата публікації:'
    )
    description = models.TextField(
        verbose_name=u'Опис:'
    )
    file_url = models.URLField(
        blank=True, 
        null=True, 
        verbose_name=u'Посилання на файл:'
    )
    file = FilerFileField(
        blank=True, 
        null=True, 
        related_name='download_file',
        verbose_name=u'Завантажити файл:'
    )
    image = FilerImageField(
        blank=True, 
        null=True, 
        related_name="book_image"
    )
    author = models.ManyToManyField(
        Author,
        blank=True,
        verbose_name=u'Автор:'
    )
    language = models.ManyToManyField(
        Language,
        blank=True,
        verbose_name=u'Мова:'
    )
    category = models.ManyToManyField(
        Category,
        blank=True,
        verbose_name=u'Категорія:'
    )
    specialty = models.ManyToManyField(
        Specialty,
        blank=True,
        verbose_name=u'Спеціальність:'
    )
    hit_count_generic = GenericRelation(
        HitCount, 
        object_id_field='object_pk',
        related_query_name='hit_count_generic_relation'
    )

    class Meta:
        verbose_name = u'Книга'
        verbose_name_plural = u'Книги'

    def __unicode__(self):
        return "%s" % self.name



