# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voud_quiz', '0003_auto_20161123_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='answers_at_end',
            field=models.BooleanField(default=False),
        ),
    ]
