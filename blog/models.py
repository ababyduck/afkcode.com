from django.db import models
from django.urls import reverse
from django.utils.text import slugify

TIME_FORMAT = '%D, %T %Z'


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'  # Django admin page will use this instead of "categorys"


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    slug = models.SlugField(default='', editable=False, max_length=255, null=False)

    def __str__(self):
        return f'{self.title} ({self.created_on.strftime(TIME_FORMAT)})'

    def get_absolute_url(self):
        kwargs = {
            'pk': self.pk,
            'slug': self.slug
        }
        return reverse('blog_detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment by {self.author} on {self.post.title} ({self.created_on.strftime(TIME_FORMAT)})'
