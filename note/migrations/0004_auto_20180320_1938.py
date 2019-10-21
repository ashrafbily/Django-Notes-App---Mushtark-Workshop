# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-20 19:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_auto_20180320_1857'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'verbose_name': 'Notes', 'verbose_name_plural': 'Notes'},
        ),
        migrations.AlterField(
            model_name='note',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
