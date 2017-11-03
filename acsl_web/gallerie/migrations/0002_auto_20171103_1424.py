# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallerie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='image_height',
            field=models.PositiveIntegerField(default=300),
        ),
        migrations.AddField(
            model_name='photo',
            name='image_width',
            field=models.PositiveIntegerField(default=320),
        ),
    ]