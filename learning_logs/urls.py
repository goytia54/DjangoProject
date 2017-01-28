"""Defines URL patterns for learning_logs."""

from django.conf.urls import url

from . import views

urlpatterns = [
    #Home page
    url(r'^$', views.index, name='index'),

    #show all topics.
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    #page for adding a new topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
]

