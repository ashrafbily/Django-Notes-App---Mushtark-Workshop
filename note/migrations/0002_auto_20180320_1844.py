# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-20 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='note',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AddField(
            model_name='note',
            name='tags',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
