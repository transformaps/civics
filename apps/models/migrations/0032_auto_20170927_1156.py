# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-27 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0031_event_google_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='google_id',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
