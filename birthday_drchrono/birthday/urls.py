from django.conf.urls import patterns, url

from birthday import views

urlpatterns = patterns('',
    url(r'^secret-email-handler?/$', views.handleEmail, name='handleEmail'),
    url(r'^$', views.index, name='index'),
)