from django.conf.urls import patterns, url

from reddit import views

urlpatterns = patterns('',
    url(r'^$', views.link_list, name='index')

)