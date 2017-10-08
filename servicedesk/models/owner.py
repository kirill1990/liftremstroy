# coding: utf-8
from django.db import models


class Owner(models.Model):

    class Meta:
        verbose_name = 'Владелец лифта'
        verbose_name_plural = 'Владелецы лифтов'

    title = models.CharField(
        'Наименование',
        max_length=256,
    )

    def __str__(self):
        return self.title
