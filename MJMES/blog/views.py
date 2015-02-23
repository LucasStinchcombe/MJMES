from django.views import generic
from django.shortcuts import render
from . import models

class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "home.html"
    paginate_by = 2

def BlogPost(request, blog_id):
    blogpost = models.Entry.objects.get(pk=blog_id)
    return render(request, 'blogpost.html', {'blogpost': blogpost})
