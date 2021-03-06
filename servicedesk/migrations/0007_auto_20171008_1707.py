# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-08 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicedesk', '0006_auto_20170827_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='elevator',
            name='address',
            field=models.CharField(blank=True, max_length=4000, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='elevator',
            name='house',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Дом'),
        ),
        migrations.AddField(
            model_name='elevator',
            name='house_id',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Кладр ID(Дом)'),
        ),
        migrations.AddField(
            model_name='elevator',
            name='street',
            field=models.CharField(blank=True, max_length=4000, null=True, verbose_name='Улица'),
        ),
        migrations.AddField(
            model_name='elevator',
            name='street_id',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Кладр ID(Улицы)'),
        ),
        migrations.AlterField(
            model_name='elevator',
            name='month_of_inspection',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Январь'), (2, 'Февраль'), (3, 'Март'), (4, 'Апрель'), (5, 'Май'), (6, 'Июнь'), (7, 'Июль'), (8, 'Август'), (9, 'Сентябрь'), (10, 'Октябрь'), (11, 'Ноябрь'), (12, 'Декабрь')], null=True, verbose_name='Месяц диагностики'),
        ),
        migrations.AlterField(
            model_name='elevator',
            name='month_of_manufacture',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Январь'), (2, 'Февраль'), (3, 'Март'), (4, 'Апрель'), (5, 'Май'), (6, 'Июнь'), (7, 'Июль'), (8, 'Август'), (9, 'Сентябрь'), (10, 'Октябрь'), (11, 'Ноябрь'), (12, 'Декабрь')], default=10, null=True, verbose_name='Месяц выпуска'),
        ),
        migrations.AlterField(
            model_name='elevator',
            name='month_of_start',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Январь'), (2, 'Февраль'), (3, 'Март'), (4, 'Апрель'), (5, 'Май'), (6, 'Июнь'), (7, 'Июль'), (8, 'Август'), (9, 'Сентябрь'), (10, 'Октябрь'), (11, 'Ноябрь'), (12, 'Декабрь')], default=10, null=True, verbose_name='Месяца запуска'),
        ),
        migrations.AlterField(
            model_name='elevator',
            name='year_of_inspection',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Год диагностики'),
        ),
    ]
