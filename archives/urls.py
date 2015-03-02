from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.ArchiveIndex.as_view(), name='archives'),
    url(r'^pdf/(?P<blog_id>\d+)/$', 'pdf'),
)
