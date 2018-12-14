from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^filer/', include('filer.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^contact-us/', views.Contact.as_view(), name='contact-us'),
    url(r'^book/', include('book.urls')),
    url(r'^category/', include('category.urls')),
    url(r'^specialty/', include('specialty.urls')),
    url(r'hitcount/', include('hitcount.urls', namespace='hitcount')),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
