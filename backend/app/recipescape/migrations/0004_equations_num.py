# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-04-03 02:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipescape', '0003_equations'),
    ]

    operations = [
        migrations.AddField(
            model_name='equations',
            name='num',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
    ]
