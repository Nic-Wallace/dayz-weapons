# Generated by Django 3.2.23 on 2023-11-22 15:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weapon',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='status',
        ),
        migrations.AddField(
            model_name='weapon',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='damage',
            field=models.PositiveIntegerField(default=10, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(150)]),
        ),
    ]
