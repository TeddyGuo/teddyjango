# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 06:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('walker', '0002_auto_20170827_0148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_at',
            new_name='created_date',
        ),
    ]