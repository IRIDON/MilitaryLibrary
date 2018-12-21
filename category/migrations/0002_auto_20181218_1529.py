# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-18 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=140, null=True, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='slug',
            field=models.SlugField(blank=True, max_length=140, null=True, unique=True, verbose_name='Slug'),
        ),
    ]