from django.db import models


class School(models.Model):
    name = models.CharField(max_length=75)
    initials = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)

    def __str__(self):
        return self.initials


class Course(models.Model):
    name = models.CharField(max_length=75)
    subject = models.CharField(max_length=10)
    code = models.CharField(max_length=5)
    units = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    school = models.ForeignKey('School', on_delete=models.PROTECT)
    completed = models.BooleanField

    def __str__(self):
        return f'{self.subject}{self.code} - {self.name}'
