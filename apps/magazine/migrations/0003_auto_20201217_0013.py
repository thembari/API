# Generated by Django 3.1.4 on 2020-12-17 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20201216_2327'),
        ('magazine', '0002_auto_20201216_2356'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issue',
            options={'ordering': ['-published_date']},
        ),
        migrations.RenameField(
            model_name='issue',
            old_name='created_on',
            new_name='published_date',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='category',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='status',
        ),
        migrations.AlterField(
            model_name='issue',
            name='slug',
            field=models.SlugField(blank=True, default='djangodbmodelsfieldscharfield', max_length=200, unique=True),
        ),
        migrations.CreateModel(
            name='Issue_Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('content', models.TextField()),
                ('category', models.CharField(max_length=200)),
                ('image', models.FileField(default='default_post.jpg', upload_to='media')),
                ('slug', models.SlugField(blank=True, default='djangodbmodelsfieldscharfield', max_length=200, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Submit')], default=0)),
                ('is_featured', models.BooleanField(default=False)),
                ('contributors', models.ManyToManyField(to='profiles.Contributor_Profile')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]