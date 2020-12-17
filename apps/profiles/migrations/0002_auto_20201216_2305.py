# Generated by Django 3.1.4 on 2020-12-16 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogpost_author'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor_profile',
            name='blog_post',
            field=models.ForeignKey(blank=True, max_length=1000, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='blog.blogpost'),
        ),
    ]
