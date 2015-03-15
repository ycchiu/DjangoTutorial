from django.conf.urls import patterns, url

from reddit import views

urlpatterns = patterns('',
    url(r'^$', views.link_list, name='index'),
    url(r'^reddit/new/$', views.link_new, name='link_new'),
    url(r'^reddit/(?P<pk>[0-9+])/edit/$', views.link_edit, name='link_edit'),
    url(r'^reddit/(?P<pk>[0-9+])/remove/$', views.link_delete, name='link_delete'),
)