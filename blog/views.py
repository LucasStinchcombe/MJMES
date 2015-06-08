from django.views import generic
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . import models

class BlogIndex(generic.ListView):
    context_object_name = 'blogposts'
    queryset = (models.Entry.objects.published())
    template_name = "home.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(BlogIndex, self).get_context_data(**kwargs)
        context['regions'] = models.Region.objects.all()
        return context

class RegionIndex(generic.ListView):
    context_object_name = 'blogposts'
    template_name = "home.html"
    paginate_by = 3

    def get_queryset(self):
        self.region = get_object_or_404(models.Region, id=self.args[0])
        return models.Entry.objects.filter(region=self.region)

    def get_context_data(self, **kwargs):
        context = super(RegionIndex, self).get_context_data(**kwargs)
        context['regions'] = models.Region.objects.all()
        return context

class TagIndex(generic.ListView):
    context_object_name = 'blogposts'
    template_name = "home.html"
    paginate_by = 3

    def get_queryset(self):
        self.tag = get_object_or_404(models.Tag, id=self.args[0])
        return models.Entry.objects.filter(tags=self.tag)

    def get_context_data(self, **kwargs):
        context = super(TagIndex, self).get_context_data(**kwargs)
        context['regions'] = models.Region.objects.all()
        return context

def BlogPost(request, blog_id):
    blogpost = models.Entry.objects.get(id=blog_id)
    return render(request, 'blogpost.html', { 'blogpost': blogpost })
