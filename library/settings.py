# -*- coding: utf-8 -*-

import os
from settings_local import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Application definition

APPS = [
    'library',
    'book',
    'specialty',
    'category',
]

INSTALLED_APPS = [
    'tinymce',
    'hitcount',
    'easy_thumbnails',
    'filer',
    'mptt',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] + APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'library.urls'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}

DATABASES['postgresql'] = POSTGRES_DATABASES


JINJA2_DIRS = [os.path.join(BASE_DIR, app, 'jinja2', app) for app in APPS]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': JINJA2_DIRS,
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'library.jinja.environment',
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'library.wsgi.application'


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'uk'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

THUMBNAIL_ALIASES = {
    '': {
        'book_cover': {'size': (250, 250), 'crop': False},
    },
}


SITE_NAME = u'Військова бібліотека'


MENU_ITEMS = [
    {
        'name': u"Головна",
        'url': "index"
    },
    {
        'name': u"Книги",
        'url': "book:index"
    },
    {
        'name': u"Категорії",
        'url': "category:index"
    },
    {
        'name': u"Cпеціальності",
        'url': "specialty:index"
    }
]


SEARCH_MIN_LENGHT = 3


PAGE_LIST_AMOUNT_BOOK = 9
PAGE_LIST_AMOUNT_CAT = 12


# Wysiwyg settings
TINYMCE_FILEBROWSER = False
TINYMCE_INCLUDE_JQUERY = False
TINYMCE_COMPRESSOR = True
TINYMCE_DEFAULT_CONFIG = {
    'mode': 'exact',
    'theme': 'advanced',
    'relative_urls': False,
    'width': 800,
    'height': 400,
    'plugins': 'table,advlink,inlinepopups,preview,searchreplace,contextmenu,paste,noneditable,visualchars,nonbreaking,xhtmlxtras',
    'theme_advanced_buttons1': 'bold,italic,underline,strikethrough,|,sub,sup,|,bullist,numlist,formatselect,|,pastetext,pasteword,|,search,replace,|,undo,redo,|,link,unlink',
    'theme_advanced_buttons2': 'visualaid,tablecontrols,|,blockquote,del,ins,|,preview,code',
    'theme_advanced_toolbar_location': 'top',
    'theme_advanced_toolbar_align': 'left',
    'content_css': '/media/css/tinymce.css',
    'extended_valid_elements': 'noindex',
    'custom_elements': 'noindex',
}

