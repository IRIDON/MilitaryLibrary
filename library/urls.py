from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap

from . import views
from category import urls

from book.sitemap import BookSitemap
from category.sitemap import CategorySitemap, SpecialtySitemap
from .sitemap import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'books': BookSitemap,
    'categories': CategorySitemap,
    'specialties': SpecialtySitemap,
}

urlpatterns = [
    url(r'^filer/', include('filer.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'hitcount/', include('hitcount.urls', namespace='hitcount')),
    url(r'^admin/', admin.site.urls),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^search/', views.Search.as_view(), name='search'),
    url(r'^book/', include('book.urls', namespace='book')),

    url(r'^contact-us/', views.Contact.as_view(), name='contact-us'),
    url(r'^thanks/', views.ContactThanks.as_view(), name='thanks'),

    url(r'^category/', include(urls.category_patterns, namespace='category')),
    url(r'^specialty/', include(urls.specialty_patterns, namespace='specialty')),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
