from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пошта')
    nickname = models.CharField(max_length=32, verbose_name="Ім'я")
    community = models.CharField(max_length=20, default='Якась громада', verbose_name='Громада')
    position = models.CharField(max_length=20, default='Чи то технік, чи то бухгалтер')
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d/', verbose_name='Аватар', blank=True)

