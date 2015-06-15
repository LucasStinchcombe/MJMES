from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from . import models
from blog.models import Background

class ArchiveIndex(generic.ListView):
    queryset = models.Archive.objects.published().order_by('-created')
    template_name = "archives.html"
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(ArchiveIndex, self).get_context_data(**kwargs)
        try:
            context['background'] = Background.objects.filter(app='AR').first()
        except Background.DoesNotExist:
            context['background'] = None

        return context


def PDF(request, archive_id):
    archive = models.Archive.objects.get(id=archive_id)
    response = HttpResponse(archive.pdf)
    response['Content-Type'] = 'application/pdf'
    response['Content-disposition'] = 'attachment'
    return response
