# Generated by Django 3.0.4 on 2020-03-16 14:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0003_auto_20200313_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='project',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
