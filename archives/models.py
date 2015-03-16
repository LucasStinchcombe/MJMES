from django.db import models
from django.utils.safestring import mark_safe

class Thumbnail(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='archives/thumbnails')
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def url(self):
        return self.image.url

    def __str__(self):
        return self.title


class ArchiveQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class Archive(models.Model):
    title = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='archives/pdf')
    thumbnail = models.ForeignKey(Thumbnail, null=True, blank=True)
    author = models.CharField(max_length=200, default="MJMES")

    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    publish = models.BooleanField(default=True)

    id = models.SlugField(max_length=200, unique=True, primary_key=True)
    objects = ArchiveQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Archived Edition"
        verbose_name_plural = "Archived Editions"
        ordering = ["created"]
