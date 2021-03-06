# Generated by Django 3.1.4 on 2020-12-17 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.contributor_profile'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.ManyToManyField(related_name='Category', to='blog.Category'),
        ),
    ]
