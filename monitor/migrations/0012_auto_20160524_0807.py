# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-24 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0011_auto_20160524_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
