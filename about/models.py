from django.db import models
from django.contrib.auth import models as auth

class Staff(models.Model):
    first = models.CharField(max_length=200)
    last = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/img/staff', null=True, blank=True)
    bio = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(auth.User, unique=True)
    def __str__(self):
        return " ".join([self.first, self.last])

    class Meta:
        verbose_name = "Staff Member"
        verbose_name_plural = "Staff Members"


class AboutUsQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class AboutUs(models.Model):
    name = models.CharField(max_length=200, default="test")
    content = models.TextField()
    publish = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True, null=True)
    modified = models.DateField(auto_now=True, null=True)

    objects = AboutUsQuerySet.as_manager()

    def __str__(self):
        return self.content
    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = verbose_name
        ordering = ['-created']
