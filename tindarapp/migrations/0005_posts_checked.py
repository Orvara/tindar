# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2020-05-16 22:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tindarapp', '0004_auto_20200516_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='checked',
            field=models.BooleanField(default=False),
        ),
    ]
