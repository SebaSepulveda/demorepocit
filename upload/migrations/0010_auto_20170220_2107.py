# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0009_auto_20170220_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='archivo',
            field=models.FileField(upload_to='media/'),
        ),
    ]