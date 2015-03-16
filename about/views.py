from django.shortcuts import render
from . import models

def About(request):
    if list(models.AboutUs.objects.published()):
        about = list(models.AboutUs.objects.published()).pop()
    else:
        about = None
    return render(request, 'about.html', { 'about': about })
