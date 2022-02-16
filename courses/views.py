from django.shortcuts import render
from courses.models import Course
from projects.models import Project


def course_index(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'course_index.html', context)


def course_detail(request, slug, pk):
    course = Course.objects.get(pk=pk)
    # projects = Project.objects.get(course=course)
    context = {
        'course': course,
        # 'projects': projects
    }
    return render(request, 'course_detail.html', context)
