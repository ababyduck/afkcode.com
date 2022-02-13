from django.shortcuts import render
from courses.models import Course


def course_index(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'course_index.html', context)


def course_detail(request, slug, pk):
    course = Course.objects.get(pk=pk)
    context = {
        'course': course
    }
    return render(request, 'course_detail.html', context)