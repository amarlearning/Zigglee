# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-28 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zigglee', '0002_auto_20160928_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
