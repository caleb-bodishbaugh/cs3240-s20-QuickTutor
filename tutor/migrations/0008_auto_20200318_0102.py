# Generated by Django 3.0.2 on 2020-03-18 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0007_jobs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobs',
            old_name='first_name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='last_name',
        ),
    ]
