# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-26 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pronos', '0003_auto_20160526_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateTimeField(db_index=True, verbose_name='Date du match'),
        ),
    ]
