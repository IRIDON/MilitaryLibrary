# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.db import models

from tinymce.models import HTMLField

from library.logic import _get_unique_slug

# Create your models here.
class Category(models.Model):
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
    slug = models.SlugField(
        max_length=settings.SLUG_MAX_LENGTH,
        unique=True,
        null=True,
        blank=True,
        verbose_name=_('Slug')
    )
    pub_date = models.DateTimeField(
        blank=False,
        auto_now=True,
        null=True,
        verbose_name=_('Дата публікації')
    )
    description = HTMLField(
        blank=True, 
        null=True,
        verbose_name=_('Опис')
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = _get_unique_slug(self.name, Category)

        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Категорію')
        verbose_name_plural = _('Категорії')

    def __unicode__(self):
        return "%s" % self.name


class Specialty(models.Model):
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
    slug = models.SlugField(
        max_length=settings.SLUG_MAX_LENGTH,
        unique=True,
        null=True,
        blank=True,
        verbose_name=_('Slug')
    )
    pub_date = models.DateTimeField(
        blank=False,
        auto_now=True,
        null=True,
        verbose_name=_('Дата публікації')
    )
    description = HTMLField(
    	blank=True,
    	null=True,
    	verbose_name=_('Опис')
	)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = _get_unique_slug(self.name, Specialty)

        super(Specialty, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Спеціальність')
        verbose_name_plural = _('Спеціальності')

    def __unicode__(self):
        return "%s" % self.name