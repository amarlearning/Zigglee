# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-28 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zigglee', '0007_auto_20160928_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cover_image',
            field=models.ImageField(upload_to=b'', verbose_name=b'./uploads/'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_thumb',
            field=models.ImageField(upload_to=b'./uploads/'),
        ),
    ]
