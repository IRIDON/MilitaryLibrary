# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-18 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, max_length=140, null=True, unique=True, verbose_name='Slug'),
        ),
    ]