from django.shortcuts import render
from . import models
from blog.models import Background

def About(request):
    try:
        about = models.AboutUs.objects.published().first()
    except models.about.DoesNotExist:
        about = None
    try:
        background = Background.objects.filter(app='AB').first()
    except Background.DoesNotExist:
        background = None

    return render(request, 'about.html', { 'about': about, 'background':background })
