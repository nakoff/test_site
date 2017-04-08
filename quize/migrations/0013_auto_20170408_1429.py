# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 07:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quize', '0012_auto_20170405_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat',
            field=models.CharField(choices=[('Спортивные', 'Спортивные'), ('Интеллектуальные', 'Интеллектуальные'), ('Творческие', 'Творческие')], max_length=200, verbose_name='категория'),
        ),
        migrations.AlterField(
            model_name='category',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quize.User', verbose_name='код'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='day',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31')], max_length=200, verbose_name='день'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='mont',
            field=models.CharField(choices=[('января', '1'), ('февраля', '2'), ('марта', '3'), ('апреля', '4'), ('мая', '5'), ('июня', '6'), ('июля', '7'), ('августа', '8'), ('сентября', '9'), ('октября', '10'), ('ноября', '11'), ('декабря', '12')], max_length=200, verbose_name='месяц'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='name',
            field=models.CharField(max_length=200, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='result',
            field=models.CharField(choices=[('первое', 'Первое'), ('второе', 'Второе'), ('третье', 'Третье'), ('участие', 'Участие')], max_length=20, verbose_name='место'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='year',
            field=models.CharField(choices=[('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017')], max_length=200, verbose_name='год'),
        ),
    ]