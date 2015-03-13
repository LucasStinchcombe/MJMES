from django.shortcuts import render
from . import models

def About(request):
    about = list(models.AboutUs.objects.published())[0]
    return render(request, 'about.html', { 'about': about })
