# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-07 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mySite', '0003_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='ip',
            field=models.CharField(default='127.0.0.1', max_length=15),
            preserve_default=False,
        ),
    ]