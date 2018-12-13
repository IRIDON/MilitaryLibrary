from django.conf.urls import url

from . import views

app_name = 'book'
urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)$', views.Detail.as_view(), name='detail'),
    url(r'^search/', views.Search.as_view(), name='search'),
]