from django.contrib import admin
from . import models
from django.contrib.auth import models as auth

from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField

class AboutUsAdmin(MarkdownModelAdmin):
    list_display = ('name', 'publish' , 'content')
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

admin.site.register(models.AboutUs, AboutUsAdmin)
admin.site.register(models.Photograph)
