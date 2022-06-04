from django.db import models
from hromady.models import CommunityHromady


class Object(models.Model):
    hromada = models.ForeignKey(CommunityHromady, on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(max_length=100, verbose_name='Адреса',blank=True)
    title = models.CharField(max_length=100, verbose_name='Назва',blank=True)
    components = models.CharField(max_length=100, verbose_name='Складові частини', blank=True)
    share_size = models.CharField(max_length=100, verbose_name='Розмір частки',blank=True)
    total_area = models.CharField(max_length=100, verbose_name='Загальна площа',blank=True)
    location = models.JSONField(verbose_name='Місцезнаходження',blank=True)
    image = models.ImageField(upload_to='image/%Y/%m/%d/', verbose_name='Зображення', blank=True)
    documents = models.FileField(upload_to='documents/%Y/%m/%d/', verbose_name='Документи', blank=True)
    class Meta:
        managed = True
        db_table = 'objects'
