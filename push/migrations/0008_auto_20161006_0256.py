# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-05 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('push', '0007_auto_20161006_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationmodel',
            name='execute_datetime',
            field=models.CharField(default='2016/10/06 02:56', max_length=16),
        ),
    ]
