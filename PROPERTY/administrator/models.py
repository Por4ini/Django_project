from django.db import models
from hromady.models import CommunityHromady


class Contacts(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ім'я", blank=True)
    role = models.CharField(max_length=60, verbose_name='Посада')
    phone = models.CharField(max_length=30, verbose_name='Номер телефону', blank=True)
    messenger = models.CharField(max_length=100, verbose_name='Мессенджер', blank=True)
    hromada = models.ForeignKey(CommunityHromady, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        verbose_name = "Контакт"
        verbose_name_plural = "Контакти"

    def __str__(self):
        return self.name


class RoleUser(models.Model):
    title = models.CharField(max_length=24, verbose_name='Роль користувача')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Роль користувача'
        verbose_name_plural = 'Ролі користувача'


class Request(models.Model):
    email = models.EmailField(('email address'), unique=True)
    hromada = models.ForeignKey(CommunityHromady, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.email
