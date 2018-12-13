from django.conf.urls import url

from . import views

app_name = 'specialty'
urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^(?P<slug>[\w-]+)/$', views.Detail.as_view(), name='detail'),
]
