# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-31 03:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_student_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='g_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]
