from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^(?P<slug>[\w-]+)/$', views.Detail.as_view(), name='detail'),
]