# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-18 10:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.file
import filer.fields.image
import hitcount.models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filer', '0010_auto_20180414_2058'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visible', models.BooleanField(default=True, verbose_name='\u041f\u043e\u043a\u0430\u0437\u0443\u0432\u0430\u0442\u0438')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430')),
                ('pub_date', models.DateTimeField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0443\u0431\u043b\u0456\u043a\u0430\u0446\u0456\u0457')),
                ('description', tinymce.models.HTMLField(verbose_name='\u041e\u043f\u0438\u0441')),
                ('file_url', models.URLField(blank=True, null=True, verbose_name='\u041f\u043e\u0441\u0438\u043b\u0430\u043d\u043d\u044f \u043d\u0430 \u0444\u0430\u0439\u043b')),
                ('author', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u0410\u0432\u0442\u043e\u0440')),
                ('category', models.ManyToManyField(blank=True, to='category.Category', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f')),
                ('file', filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='download_file', to='filer.File', verbose_name='\u0417\u0430\u0432\u0430\u043d\u0442\u0430\u0436\u0438\u0442\u0438 \u0444\u0430\u0439\u043b')),
                ('image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_image', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'verbose_name': '\u041a\u043d\u0438\u0433\u0443',
                'verbose_name_plural': '\u041a\u043d\u0438\u0433\u0438',
            },
            bases=(models.Model, hitcount.models.HitCountMixin),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430:')),
                ('iso', models.CharField(max_length=2, unique=True, verbose_name='ISO \u043a\u0440\u0430\u0457\u043d\u0438')),
            ],
            options={
                'verbose_name': '\u041c\u043e\u0432\u0443',
                'verbose_name_plural': '\u041c\u043e\u0432\u0438',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ManyToManyField(blank=True, to='book.Language', verbose_name='\u041c\u043e\u0432\u0430'),
        ),
        migrations.AddField(
            model_name='book',
            name='specialty',
            field=models.ManyToManyField(blank=True, to='category.Specialty', verbose_name='\u0421\u043f\u0435\u0446\u0456\u0430\u043b\u044c\u043d\u0456\u0441\u0442\u044c'),
        ),
    ]
