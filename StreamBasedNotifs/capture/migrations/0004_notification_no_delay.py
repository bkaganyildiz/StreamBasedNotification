# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capture', '0003_auto_20170429_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='no_delay',
            field=models.BooleanField(default=False),
        ),
    ]