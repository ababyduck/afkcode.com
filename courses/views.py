from django.shortcuts import render
from courses.models import Course
from projects.models import Project


def course_index(request):
    courses_in_progress = Course.objects.filter(in_progress=True).order_by('school', 'subject', 'code')
    courses_completed = Course.objects.filter(completed=True).order_by('school', 'subject', 'code')
    courses_other = Course.objects.filter(in_progress=False, completed=False).order_by('school', 'subject', 'code')
    context = {
        'courses_in_progress': courses_in_progress,
        'courses_completed': courses_completed,
        'courses_other': courses_other
    }
    return render(request, 'course_index.html', context)


def course_detail(request, slug, pk):
    course = Course.objects.get(pk=pk)
    projects = Project.objects.filter(course=course)
    context = {
        'course': course,
        'projects': projects
    }
    return render(request, 'course_detail.html', context)
