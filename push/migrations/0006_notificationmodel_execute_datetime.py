# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-05 15:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('push', '0005_auto_20161003_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationmodel',
            name='execute_datetime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
