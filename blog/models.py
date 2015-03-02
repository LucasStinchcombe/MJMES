from django.db import models

class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.slug

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/img', height_field='height', width_field='width')
    width = models.IntegerField(editable=False)
    height = models.IntegerField(editable=False)

    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Entry(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ForeignKey(Image, default=1)
    tags = models.ManyToManyField(Tag)

    publish = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True)

    objects = EntryQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]
