from django.views import generic
from django.shortcuts import render
from . import models

class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "home.html"
    paginate_by = 3

def BlogPost(request, blog_id):
    blogpost = models.Entry.objects.get(id=blog_id)
    return render(request, 'blogpost.html', { 'blogpost': blogpost })
