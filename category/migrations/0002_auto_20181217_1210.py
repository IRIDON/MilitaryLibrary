# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-17 10:10
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044e', 'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u0457'},
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='\u041e\u043f\u0438\u0441:'),
        ),
    ]