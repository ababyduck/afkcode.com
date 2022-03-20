from django.shortcuts import render
from courses.models import Course, School
from projects.models import Project


def course_index(request, filter_by_school=''):
    if filter_by_school:
        all_courses = Course.objects.filter(school__initials=filter_by_school.upper())
    else:
        all_courses = Course.objects.all().order_by('school__name')
    courses_in_progress = all_courses.filter(status=Course.Status.IN_PROGRESS).order_by('subject', 'code')
    courses_completed = all_courses.filter(status=Course.Status.COMPLETED).order_by('year', 'semester')
    courses_planned = all_courses.filter(status=Course.Status.PLANNED).order_by('year', 'semester')

    school_list = School.objects.values('name', 'initials').order_by('name')

    context = {
        'courses_in_progress': courses_in_progress,
        'courses_completed': courses_completed,
        'courses_planned': courses_planned,
        'filter_by_school': filter_by_school,
        'school_list': school_list
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
