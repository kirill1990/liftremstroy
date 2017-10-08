# coding: utf-8
from django.db import models


class Incident(models.Model):

    class Meta:
        verbose_name = 'Инцидент'
        verbose_name_plural = 'Инциденты'

    title = models.CharField(
        'Название',
        max_length=256,
    )

    description = models.TextField(
        'Описание',
        null=True,
        blank=True,
    )

    status = models.PositiveSmallIntegerField(
        'Статус',
        choices=(
            (1, 'Открыта'),
            (2, 'В работе'),
            (3, 'Решен'),
        ),
        default=1,
    )

    start_time = models.DateTimeField(
        'Время поступления заявки',
        null=True,
        blank=True,
    )

    finish_time = models.DateTimeField(
        'Время выполнения заявки',
        null=True,
        blank=True,
    )

    time_created = models.DateTimeField(
        'Дата и время создания',
        auto_now_add=True,
    )

    time_updated = models.DateTimeField(
        'Дата и время обновления',
        auto_now=True,
    )

    user_created = models.ForeignKey(
        'auth.User',
        blank=True,
        null=True,
        related_name='user_created',

    )

    user_updated = models.ForeignKey(
        'auth.User',
        blank=True,
        null=True,
        related_name='user_updated',
    )

    def __str__(self):
        return '[%i] %s' % (self.id, self.title)

    def get_absolute_url(self):
        # from django.urls import reverse
        # return reverse('people.views.details', args=[str(self.id)])
        return "/people/%i/" % self.id

