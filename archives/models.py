from django.db import models

class ArchiveQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class Archive(models.Model):
    id = models.SlugField(max_length=200, unique=True, primary_key=True)
    title = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='static/pdf')
    author = models.CharField(max_length=200, default="MJMES")

    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    publish = models.BooleanField(default=True)

    objects = ArchiveQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Archived Edition"
        verbose_name_plural = "Archived Editions"
        ordering = ["-created"]
