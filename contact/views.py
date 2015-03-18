from django.shortcuts import render
from . import models

def Contact(request):
    if list(models.ContactUs.objects.published()):
        contact = list(models.ContactUs.objects.published()).pop()
    else:
        contact = None
    return render(request, 'contact.html', { 'contact': contact })
