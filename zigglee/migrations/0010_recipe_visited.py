# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-28 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zigglee', '0009_auto_20160928_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='visited',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
