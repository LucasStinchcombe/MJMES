from django.views import generic
from django.shortcuts import render
from . import models

class BlogIndex(generic.ListView):
    context_object_name = 'blogposts'
    queryset = (models.Entry.objects.published())
    template_name = "home.html"
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(BlogIndex, self).get_context_data(**kwargs)
        context['tags'] = models.Tag.objects.all()
        return context

def BlogPost(request, blog_id):
    blogpost = models.Entry.objects.get(id=blog_id)
    return render(request, 'blogpost.html', { 'blogpost': blogpost })
