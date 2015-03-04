from django.contrib import admin
from . import models

class ArchiveAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'created')
    prepopulated_fields = {'id':('title',)}

admin.site.register(models.Archive, ArchiveAdmin)
