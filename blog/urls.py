from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.BlogIndex.as_view(), name='index'),
    url(r'^blogpost/(?P<blog_id>[a-zA-Z0-9_.-]+)/$', views.BlogPost, name='blogpost'),
)
