# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quize', '0005_auto_20170404_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]
