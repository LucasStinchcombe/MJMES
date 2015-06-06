from django.db import models
from django.contrib.auth import models as auth

def markdown_to_html( markdownText, images ):
    image_ref = ""
    for image in images:
        image_url = image.image.url
        image_ref = "%s\n[%s]: %s" % (image_ref, image, image_url)

    markdown = "%s\n%s" % (markdownText, image_ref)
    return markdown

class Photograph(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='about/img')
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def url(self):
        return self.image.url

    class Meta:
        verbose_name = 'Photograph'
        verbose_name_plural = 'Photographs'


class AboutUsQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class AboutUs(models.Model):
    name = models.CharField(max_length=200, default="test")
    content = models.TextField()
    images = models.ManyToManyField(Photograph, null=True, blank=True)
    publish = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True, null=True)
    modified = models.DateField(auto_now=True, null=True)

    objects = AboutUsQuerySet.as_manager()

    def __str__(self):
        return self.name

    def markdown(self):
        return markdown_to_html(self.content, self.images.all())

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = verbose_name
        ordering = ['-created']
