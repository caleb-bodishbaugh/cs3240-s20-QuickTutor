# Generated by Django 3.0.2 on 2020-03-28 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0002_auto_20200328_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='isConfirmed',
            field=models.BooleanField(default=True),
        ),
    ]
