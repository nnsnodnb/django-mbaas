# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-11-15 23:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('push', '0013_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationmodel',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='notificationmodel',
            name='execute_datetime',
            field=models.CharField(default='2016/11/15 23:10', max_length=16),
        ),
    ]