# Generated by Django 3.2.23 on 2023-12-02 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20231122_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='weapon',
            name='slug',
            field=models.SlugField(default='name', max_length=200, unique=True),
        ),
    ]