# Generated by Django 3.1.4 on 2020-12-20 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0005_auto_20201220_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='magazine.issue'),
        ),
    ]