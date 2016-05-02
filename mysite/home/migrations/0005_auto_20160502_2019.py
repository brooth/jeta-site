# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-02 20:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20160306_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='markdownpage',
            name='modified_ts',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='markdownpage',
            name='path',
            field=models.CharField(blank=True, max_length=140, unique=True),
        ),
    ]
