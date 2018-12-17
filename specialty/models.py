# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import gettext as _
from django.db import models

from tinymce.models import HTMLField

# Create your models here.
class Specialty(models.Model):
    name = models.CharField(
        blank=False, 
        null=True, 
        max_length=100,
        verbose_name=_('Назва')
    )
    slug = models.SlugField(
        max_length=25,
        null=False,
        blank=False,
        unique=True,
        verbose_name='Slug',
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

    class Meta:
        verbose_name = _('Спеціальність')
        verbose_name_plural = _('Спеціальності')

    def __unicode__(self):
        return "%s" % self.name