from django.db import models
from objects.models import Object


class Subjects(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE, blank=True, verbose_name="Об'єкт")
    status = models.BooleanField(default=False)
    balance_holder = models.CharField(max_length=120, verbose_name="Орендар/Балансоутримувач")
    title = models.CharField(max_length=120, verbose_name='Назва')
    components = models.CharField(max_length=120, verbose_name='Складові частини')
    part_size = models.CharField(max_length=120, verbose_name='Розмір частки')
    area = models.CharField(max_length=120, verbose_name='Площа')
    period_of_use = models.CharField(max_length=120, verbose_name='Період користування')
    extra = models.CharField(max_length=400, blank=True, verbose_name="Додаткова інформація")

    class Meta:
        verbose_name = "Суб'єкт"
        verbose_name_plural = "Суб'єкти"

    def __str__(self):
        return self.title


class SubjectImages(models.Model):
    title = models.CharField(max_length=40, verbose_name='Назва')
    image = models.ImageField(upload_to='image/%Y/%m/%d/', verbose_name='Зображення')
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        verbose_name = "Зображення cуб'єкт"
        verbose_name_plural = "Зображення cуб'єкта"

    def __str__(self):
        return self.title


class SubjectDocuments(models.Model):
    title = models.CharField(max_length=40, verbose_name='Назва')
    documents = models.FileField(upload_to='documents/%Y/%m/%d/', verbose_name='Документи')
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        verbose_name = "Документ cуб'єкт"
        verbose_name_plural = "Документи cуб'єкта"

    def __str__(self):
        return self.title
