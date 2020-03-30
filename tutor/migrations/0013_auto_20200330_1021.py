# Generated by Django 3.0.4 on 2020-03-30 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0012_merge_20200329_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(blank=True, default='default_profile_pic.png', help_text='Uploading a profile picture makes it easier for your tutor/student to recognize you.', upload_to='profile_picture'),
        ),
    ]
