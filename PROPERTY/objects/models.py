from django.db import models
from hromady.models import CommunityHromady


class Object(models.Model):
    hromada = models.ForeignKey(CommunityHromady, on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(max_length=100, verbose_name='Адреса', blank=True)
    title = models.CharField(max_length=100, verbose_name='Назва', blank=True)
    components = models.CharField(max_length=100, verbose_name='Складові частини', blank=True)
    share_size = models.CharField(max_length=100, verbose_name='Розмір частки', blank=True)
    total_area = models.CharField(max_length=100, verbose_name='Загальна площа', blank=True)
    location = models.JSONField(verbose_name='Місцезнаходження', blank=True, null=True)
    extra = models.CharField(max_length=400, blank=True, verbose_name="Додаткова інформація")

    class Meta:
        managed = True
        db_table = 'objects'
        verbose_name = "Об'єкт"
        verbose_name_plural = "Об'єкти"

    def __str__(self):
        return self.title


class ObjectImages(models.Model):
    title = models.CharField(max_length=40, verbose_name='Назва')
    image = models.ImageField(upload_to='image/%Y/%m/%d/', verbose_name='Зображення')
    object = models.ForeignKey(Object, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        verbose_name = "Зображення об'єкта"
        verbose_name_plural = "Зображення об'єкта"

    def __str__(self):
        return self.title


class ObjectDocuments(models.Model):
    title = models.CharField(max_length=40, verbose_name='Назва')
    documents = models.FileField(upload_to='documents/%Y/%m/%d/', verbose_name='Документи')
    object = models.ForeignKey(Object, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        verbose_name = "Документ об'єкта"
        verbose_name_plural = "Документи об'єкта"

    def __str__(self):
        return self.title
