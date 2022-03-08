from django.shortcuts import render
from projects.models import Project


def project_index(request):
    projects = Project.objects.all().order_by('-sorting_priority', '-date', 'title')
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk, slug):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
