# Generated by Django 4.0.2 on 2022-02-13 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='school_logos/'),
        ),
    ]
