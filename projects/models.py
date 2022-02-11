import os
from django.db import models
from afkcode.settings import STATIC_ROOT


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path=os.path.join(STATIC_ROOT, 'img/'))

    def __str__(self):
        return self.title
