import markdown
from django.db import models
from about import models as about
from django.conf import settings
from django.apps import apps

def markdown_to_html( markdownText, images ):
    image_ref = ""
    for image in images:
        image_url = image.image.url
        image_ref = "%s\n[%s]: %s" % (image_ref, image, image_url)

    markdown = "%s\n%s" % (markdownText, image_ref)
    return markdown


class Tag(models.Model):
    tag = models.CharField(max_length=200)
    id = models.SlugField(max_length=200, unique=True, primary_key=True)

    def __str__(self):
        return self.tag


class Region(models.Model):
    region = models.CharField(max_length=200, unique=True)
    id = models.SlugField(max_length=200, unique=True, primary_key=True)

    def __str__(self):
        return self.region


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog/img')
    caption = models.TextField(null=True, blank=True)
    created = models.DateField()
    modified = models.DateField(auto_now=True)

    def url(self):
        return self.image.url

    def __str__(self):
        return self.title


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)
    def hasTag(tag,self):
        return self.filter(tags=tag)


class Entry(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    body = models.TextField()
    photograph = models.ForeignKey(Image, unique=True, related_name='main photograph')
    author = models.CharField(max_length=200)
    images = models.ManyToManyField(Image, blank=True, related_name='figures and tables')
    tags = models.ManyToManyField(Tag)
    region = models.ManyToManyField(Region)

    publish = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    id = models.SlugField(max_length=200, unique=True, primary_key=True)
    objects = EntryQuerySet.as_manager()

    def __str__(self):
        return self.title

    def markdown(self):
        return markdown_to_html(self.body, self.images.all())

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]

class Background(models.Model):
    title = models.CharField(max_length=200)
    background = models.ImageField(upload_to='blog/backgrounds')

    ABOUT = 'AB'
    ARCHIVES = 'AR'
    BLOG = 'BL'
    CONTACT = 'CO'
    NONE = 'NO'

    APP_CHOICES = (
        (ABOUT, 'About'),
        (ARCHIVES, 'Archives'),
        (BLOG, 'Blog'),
        (CONTACT, 'Contact'),
        (NONE, 'None')
    )

    app = models.CharField(max_length=2, choices=APP_CHOICES, default=NONE)

    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)


    def url(self):
        return self.background.url

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["app","title"]
