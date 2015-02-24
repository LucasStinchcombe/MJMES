from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.BlogIndex.as_view(), name='index'),
    url(r'^blogpost/(?P<blog_id>\d+)/$', views.BlogPost, name='blogpost'),
)
