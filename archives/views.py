from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from . import models

class ArchiveIndex(generic.ListView):
    queryset = models.Archive.objects.published()
    template_name = "archives.html"
    paginate_by = 3

def PDF(request, file_id):
    archive = models.Archive.objects.get(id=file_id)

    response = HttpResponse(archive.pdf)
    response['Content-Type'] = 'application/pdf'
    response['Content-disposition'] = 'attachment'
    return response
