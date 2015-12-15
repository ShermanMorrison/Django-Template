from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^(?P<pk>\d+)/$', views.chat_room, name='chat_room'),
)