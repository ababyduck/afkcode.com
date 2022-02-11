from django.contrib import admin
from courses.models import School, Course


class SchoolAdmin(admin.ModelAdmin):
    pass


class CourseAdmin(admin.ModelAdmin):
    pass


admin.site.register(School, SchoolAdmin)
admin.site.register(Course, CourseAdmin)
