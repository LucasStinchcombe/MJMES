from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.ArchiveIndex.as_view(), name='archives'),
    url(r'^pdf/(?P<archive_id>[a-zA-Z0-9_.-]+)/$', views.PDF, name='pdf_download'),
)
