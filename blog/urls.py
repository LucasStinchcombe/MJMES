from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.BlogIndex.as_view(), name='index'),
    url(r'^blogpost/(?P<blog_id>[a-zA-Z0-9_.-]+)/$', views.BlogPost, name='blogpost'),
    url(r'^region/([a-zA-Z0-9_.-]+)/$', views.RegionIndex.as_view(), name='region' ),
    url(r'^tag/([a-zA-Z0-9_.-]+)/$', views.TagIndex.as_view(), name='tag' )
)
