from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    course = models.ForeignKey('courses.Course', on_delete=models.SET_NULL, null=True, blank=True)
    categories = models.ManyToManyField('blog.Category')

    def __str__(self):
        return self.title
