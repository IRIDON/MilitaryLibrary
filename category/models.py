# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(
        blank=False, 
        null=True, 
        max_length=100,
        verbose_name=u'Назва:'
    )
    slug = models.SlugField(
        max_length=25,
        null=False,
        blank=False,
        unique=True,
        verbose_name=u'Slug:'
    )
    pub_date = models.DateTimeField(
        blank=False,
        auto_now=True,
        null=True,
        verbose_name=u'Дата публікації:'
    )
    description = models.TextField(
        blank=True, 
        null=True,
        verbose_name=u'Опис:'
    )

    class Meta:
        verbose_name = u'Категорія'
        verbose_name_plural = u'Категорії'

    def __unicode__(self):
        return "%s" % self.name