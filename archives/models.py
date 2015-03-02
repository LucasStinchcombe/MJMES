from django.db import models

class ArchiveQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class Archive(models.Model):
    title = models.CharField(max_length=200, primary_key=True)
    pdf = models.FileField(upload_to='static/pdf')
    author = models.CharField(max_length=200, default="MJMES")

    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    publish = models.BooleanField(default=True)

    objects = ArchiveQuerySet.as_manager()

    class Meta:
        verbose_name = "Archived Edition"
        verbose_name_plural = "Archived Editions"
        ordering = ["-created"]
