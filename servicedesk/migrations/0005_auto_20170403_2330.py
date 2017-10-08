# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-03 20:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('servicedesk', '0004_auto_20170403_2258'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Открыта'), (2, 'В работе'), (3, 'Решен')], default=1, verbose_name='Статус')),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name='Время поступления заявки')),
                ('finish_time', models.DateTimeField(blank=True, null=True, verbose_name='Время выполнения заявки')),
                ('time_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('time_updated', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
                ('user_created', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_created', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Инцидент',
                'verbose_name_plural': 'Инциденты',
            },
        ),
        migrations.DeleteModel(
            name='Journal',
        ),
    ]
