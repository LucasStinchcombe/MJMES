from django.shortcuts import render
from . import models

def about(request):
    about = list(models.AboutUs.objects.published())[0]
    return render(request, 'about.html', { 'about':about })
    
