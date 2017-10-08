# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-26 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicedesk', '0002_journal'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='description',
            field=models.CharField(blank=True, max_length=4096, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='journal',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Открыта'), (2, 'В работе'), (3, 'Решен')], default=1, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
    ]
