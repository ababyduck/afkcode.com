from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class School(models.Model):
    name = models.CharField(max_length=60)
    initials = models.CharField(max_length=10)
    logo = models.ImageField(upload_to='school_logos/', null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=60)
    subject = models.CharField(max_length=10)
    code = models.CharField(max_length=5)
    units = models.PositiveSmallIntegerField()
    description = models.TextField(null=True, blank=True)
    school = models.ForeignKey('School', on_delete=models.PROTECT)
    categories = models.ManyToManyField('blog.Category')
    slug = models.SlugField(default='', editable=False, max_length=25, null=False)

    class Status(models.IntegerChoices):
        PLANNED = 1
        IN_PROGRESS = 2
        COMPLETED = 3
    status = models.IntegerField(choices=Status.choices, default=Status.PLANNED)

    class Semester(models.IntegerChoices):
        SPRING_A = 1
        SPRING_B = 2
        SUMMER_A = 3
        SUMMER_B = 4
        FALL_A = 5
        FALL_B = 6
    semester = models.IntegerField(choices=Semester.choices, blank=True, null=True)
    year = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.school.initials}: {self.subject}{self.code} - {self.name}'

    def get_absolute_url(self):
        kwargs = {
            'pk': self.pk,
            'slug': self.slug
        }
        return reverse('course_detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = f'{self.school.initials}-{self.subject}{self.code}'
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class Credential(models.Model):
    major = models.CharField(max_length=60)
    type = models.CharField(max_length=60)
    type_letters = models.CharField(max_length=5, null=True, blank=True)
    school = models.ForeignKey('School', related_name='credentials', on_delete=models.PROTECT)

    def __str__(self):
        if self.type_letters is None:
            prefix = self.type
        else:
            prefix = self.type_letters
        return f'{prefix} in {self.major} from {self.school.initials}'
