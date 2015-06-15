from django.contrib import admin
from . import models

from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField

class EntryAdmin(MarkdownModelAdmin):
    list_display = ('title', 'author', 'created')
    prepopulated_fields = {'id':('title',)}
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

class BackgroundAdmin(MarkdownModelAdmin):
    list_display = ('title', 'app')

admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.Image)
admin.site.register(models.Region)
admin.site.register(models.Tag)
admin.site.register(models.Background, BackgroundAdmin)
