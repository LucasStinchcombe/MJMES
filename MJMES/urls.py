from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog import views
from archives import views
from about import views

urlpatterns = patterns(
    '',
    url(r'^', include('blog.urls')),
    url(r'^about/',include('about.urls')),
    url(r'^archives/',include('archives.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),
)
