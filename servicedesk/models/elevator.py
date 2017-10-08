# coding: utf-8
import datetime

from django.db import models
from servicedesk.models.owner import Owner


class Elevator(models.Model):

    MONTH_CHOICES = (
        (1, "Январь"),
        (2, "Февраль"),
        (3, "Март"),
        (4, "Апрель"),
        (5, "Май"),
        (6, "Июнь"),
        (7, "Июль"),
        (8, "Август"),
        (9, "Сентябрь"),
        (10, "Октябрь"),
        (11, "Ноябрь"),
        (12, "Декабрь"),
    )

    class Meta:
        verbose_name = 'Лифт'
        verbose_name_plural = 'Лифты'

    owner = models.ForeignKey(
        Owner
    )

    # адрес

    address = models.CharField(
        'Адрес',
        max_length=4000,
        null=True,
        blank=True,
    )

    street = models.CharField(
        'Улица',
        max_length=4000,
        null=True,
        blank=True,
    )

    street_id = models.CharField(
        'Кладр ID(Улицы)',
        max_length=1000,
        null=True,
        blank=True,
    )

    house = models.CharField(
        'Дом',
        max_length=1000,
        null=True,
        blank=True,
    )

    house_id = models.CharField(
        'Кладр ID(Дом)',
        max_length=1000,
        null=True,
        blank=True,
    )

    entrance = models.CharField(
        'Подъезд',
        max_length=1000,
        null=True,
        blank=True,
    )

    floors = models.CharField(
        'Этажей',
        max_length=1000,
        null=True,
        blank=True,
    )

    serial_number = models.CharField(
        'Заводской номер',
        max_length=128,
        null=True,
        blank=True,
    )

    reg_number = models.CharField(
        'Рег. номер',
        max_length=128,
        null=True,
        blank=True,
    )

    capacity = models.PositiveIntegerField(
        'Грузоподъемность',
        null=True,
        blank=True,
    )

    speed = models.PositiveIntegerField(
        'Скорость. м/с',
        null=True,
        blank=True,
    )

    year_of_manufacture = models.PositiveSmallIntegerField(
        'Год выпуска',
        default=datetime.date.today().year,
        null=True,
        blank=True,
    )

    month_of_manufacture = models.PositiveSmallIntegerField(
        'Месяц выпуска',
        default=datetime.date.today().month,
        choices=MONTH_CHOICES,
        null=True,
        blank=True,
    )

    year_of_start = models.PositiveSmallIntegerField(
        'Год запуска',
        default=datetime.date.today().year,
        null=True,
        blank=True,
    )

    month_of_start = models.PositiveSmallIntegerField(
        'Месяца запуска',
        default=datetime.date.today().month,
        choices=MONTH_CHOICES,
        null=True,
        blank=True,
    )

    name_of_manufacture = models.CharField(
        'Изготовитель',
        max_length=128,
        null=True,
        blank=True,
    )

    periodiki = models.PositiveSmallIntegerField(
        'Отметки переодики',
        choices=MONTH_CHOICES,
        null=True,
        blank=True,
    )

    month_of_inspection = models.PositiveSmallIntegerField(
        'Месяц диагностики',
        choices=MONTH_CHOICES,
        null=True,
        blank=True,
    )

    year_of_inspection = models.PositiveSmallIntegerField(
        'Год диагностики',
        null=True,
        blank=True,
    )

    payment = models.CharField(
        'Оплата',
        max_length=128,
        null=True,
        blank=True,
    )

    prorab = models.CharField(
        'Прораб',
        max_length=128,
        null=True,
        blank=True,
    )

    elmechanik = models.CharField(
        'Эл.Механик',
        max_length=128,
        null=True,
        blank=True,
    )

    make = models.CharField(
        'Марка лифта',
        max_length=128,
        null=True,
        blank=True,
    )

    st_upr = models.CharField(
        'Ст.Упр.',
        max_length=128,
        null=True,
        blank=True,
    )

    communication = models.CharField(
        'Связь',
        max_length=128,
        null=True,
        blank=True,
    )

    lifterka = models.CharField(
        'Лифтерка',
        max_length=128,
        null=True,
        blank=True,
    )

    schema = models.CharField(
        'Схема',
        max_length=128,
        null=True,
        blank=True,
    )

    kanat = models.CharField(
        'Канаты',
        max_length=128,
        null=True,
        blank=True,
    )

    kvh = models.CharField(
        'КВШ',
        max_length=128,
        null=True,
        blank=True,
    )

    reductor = models.CharField(
        'Редуктор',
        max_length=128,
        null=True,
        blank=True,
    )

    engine = models.CharField(
        'Двигатель',
        max_length=128,
        null=True,
        blank=True,
    )

    def __str__(self):
        return '%s [%s]' % (self.address, self.entrance)

    def get_absolute_url(self):
        # from django.urls import reverse
        # return reverse('people.views.details', args=[str(self.id)])
        return "elevators/%i/" % self.id
