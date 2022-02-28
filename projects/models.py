from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from afkcode.utils import image_resize


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    course = models.ForeignKey('courses.Course', on_delete=models.SET_NULL, null=True, blank=True)
    categories = models.ManyToManyField('blog.Category')
    slug = models.SlugField(default='', editable=False, max_length=100, null=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'pk': self.pk,
            'slug': self.slug
        }
        return reverse('project_detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        # Generate slug url
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        # Resize image if necessary
        image_resize(self.image, 900, 600)

        super().save(*args, **kwargs)
