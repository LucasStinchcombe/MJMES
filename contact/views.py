from django.shortcuts import render
from . import models
from blog.models import Background

def Contact(request):
    try:
        contact = models.ContactUs.objects.published().first()
    except models.ContactUs.DoesNotExist:
        contact = None
    try:
        background = Background.objects.filter(app='CO').first()
    except Background.DoesNotExist:
        background = None
    return render(request, 'contact.html', { 'contact': contact, 'background': background })
