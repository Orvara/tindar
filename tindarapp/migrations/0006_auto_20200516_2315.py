# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2020-05-16 23:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tindarapp', '0005_posts_checked'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='checked',
            new_name='lesid',
        ),
    ]
