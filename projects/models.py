import os
from django.db import models

from afkcode.settings import STATIC_ROOT


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FilePathField(path=os.path.join(STATIC_ROOT, 'img/'), null=True, blank=True)
    course = models.ForeignKey('courses.Course', on_delete=models.SET_NULL, null=True, blank=True)
    categories = models.ManyToManyField('blog.Category', null=True, blank=True)

    def __str__(self):
        return self.title
