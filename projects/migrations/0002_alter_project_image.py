# Generated by Django 4.0.2 on 2022-02-12 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(upload_to='uploads/% Y/% m/% d/'),
        ),
    ]
