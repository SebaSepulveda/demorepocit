# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0008_auto_20170220_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='archivo',
            field=models.FileField(upload_to='documents/'),
        ),
    ]
