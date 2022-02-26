from django.shortcuts import render
from courses.models import Course
from projects.models import Project


def course_index(request):
    all_courses = Course.objects.all()
    courses_in_progress = all_courses.filter(in_progress=True).order_by('school', 'subject', 'code')
    courses_completed = all_courses.filter(completed=True).order_by('school', 'subject', 'code')
    courses_planned = all_courses.filter(in_progress=False, completed=False).order_by('school', 'subject', 'code')
    context = {
        'courses_in_progress': courses_in_progress,
        'courses_completed': courses_completed,
        'courses_planned': courses_planned
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
