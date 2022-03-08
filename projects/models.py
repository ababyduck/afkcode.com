from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from afkcode.utils import image_resize
from blog.models import Category


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/', null=True, blank=True)
    image_alt_text = models.CharField(max_length=100, null=True, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    course = models.ForeignKey('courses.Course', null=True, blank=True, on_delete=models.SET_NULL)
    slug = models.SlugField(default='', editable=False, max_length=100)
    date = models.DateField(default=timezone.now)
    sorting_priority = models.SmallIntegerField(default=0,
                                                help_text='A high sorting priority causes projects to be displayed '
                                                          'first in the index view, while a negative value places '
                                                          'them at the end. Default is 0.')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'pk': self.pk,
            'slug': self.slug
        }
        return reverse('project_detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)

        # Resize image before uploading if it exceeds given dimensions
        try:
            image_resize(self.image, 900, 600)
        except ValueError:
            # Nothing to resize if image field is null
            pass

        super(Project, self).save(*args, **kwargs)
