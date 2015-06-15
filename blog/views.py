from django.views import generic
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . import models

class BaseIndex(generic.ListView):
    context_object_name = 'blogposts'
    template_name = 'home.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(BaseIndex, self).get_context_data(**kwargs)
        context['regions'] = models.Region.objects.all()
        try:
            context['background'] = models.Background.objects.filter(app='BL').first()
        except models.Background.DoesNotExist:
            context['background'] = None

        return context

    class Meta:
        abstract = True

class BlogIndex(BaseIndex):
    def get_queryset(self):
        return models.Entry.objects.published()

class RegionIndex(BaseIndex):
    def get_queryset(self):
        self.region = get_object_or_404(models.Region, id=self.args[0])
        return models.Entry.objects.filter(region=self.region)

class TagIndex(BaseIndex):
    def get_queryset(self):
        self.tag = get_object_or_404(models.Tag, id=self.args[0])
        return models.Entry.objects.filter(tags=self.tag)


def BlogPost(request, blog_id):
    blogpost = models.Entry.objects.get(id=blog_id)
    return render(request, 'blogpost.html', { 'blogpost': blogpost })
