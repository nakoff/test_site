# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 07:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quize', '0013_auto_20170408_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quize.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user',
            field=models.CharField(max_length=50, verbose_name='код'),
        ),
    ]