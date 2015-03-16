from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^', include('blog.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^archives/',include('archives.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),
    # url(r'^(?P<page_id>[a-zA-Z0-9_.-]+)/$',include('pages.urls')),
)
