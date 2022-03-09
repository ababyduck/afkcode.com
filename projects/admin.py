from django.contrib import admin
from projects.models import Project


class ProjectAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'


admin.site.register(Project, ProjectAdmin)
