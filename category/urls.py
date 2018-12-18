from django.conf.urls import url, include

from . import views

category_patterns = [
    url(r'^$', views.CategoryIndex.as_view(), name='index'),
    url(r'^(?P<slug>[\w-]+)/$', views.CategoryDetail.as_view(), name='detail'),
]

specialty_patterns = [
    url(r'^$', views.SpecialtyIndex.as_view(), name='index'),
    url(r'^(?P<slug>[\w-]+)/$', views.SpecialtyDetail.as_view(), name='detail'),
]
