# Generated by Django 3.1.4 on 2020-12-20 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201217_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=40),
        ),
    ]
