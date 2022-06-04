from django.db import models
from objects.models import Object


class Subjects(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE, blank=True, verbose_name="Об'экт")
    status = models.BooleanField(default=False)
    balance_holder = models.CharField(max_length=120, verbose_name="Орендар/Балансоутримувач")
    title = models.CharField(max_length=120, verbose_name='Назва')
    components = models.CharField(max_length=120, verbose_name='Складові частини')
    part_size = models.CharField(max_length=120, verbose_name='Розмір частки')
    area = models.CharField(max_length=120, verbose_name = 'Площа')
    period_of_use = models.CharField(max_length=120, verbose_name='Період користування')
    image = models.ImageField(upload_to='image/%Y/%m/%d/', verbose_name='Зображення', blank=True)
    documents = models.FileField(upload_to='documents/%Y/%m/%d/', verbose_name='Документи', blank=True)