# Generated by Django 4.0.2 on 2022-02-12 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_image'),
        ('courses', '0003_alter_course_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='completed',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='projects',
            field=models.ManyToManyField(related_name='course', to='projects.Project'),
        ),
    ]
