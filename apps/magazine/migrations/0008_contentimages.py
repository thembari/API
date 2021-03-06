# Generated by Django 3.1.4 on 2020-12-22 15:55

import apps.magazine.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0007_auto_20201220_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentImages',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to=apps.magazine.models.get_image_filename)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magazine.content')),
            ],
        ),
    ]
