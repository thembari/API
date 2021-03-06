# Generated by Django 3.1.4 on 2020-12-17 03:12

import apps.profiles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor_profile',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='contributor_profile',
            name='image',
            field=models.FileField(default='default_imgs/default_male.jpg', upload_to=apps.profiles.models.contributor_photo_path),
        ),
    ]
