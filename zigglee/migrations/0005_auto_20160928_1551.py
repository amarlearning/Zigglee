# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-28 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zigglee', '0004_auto_20160928_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_method',
            field=models.TextField(max_length=15000),
        ),
    ]
