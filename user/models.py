from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from hromady.models import CommunityHromady
from .manager import CustomUserManager
from administrator.models import RoleUser


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    community = models.ForeignKey(CommunityHromady, verbose_name="Громада", on_delete=models.CASCADE, default=1,
                                  blank=True, null=True)
    photo = models.ImageField(upload_to='image/photo/%Y/%m/%d/', verbose_name='Авка', blank=True,
                              default='image/ava.png')
    extra = models.CharField(max_length=400, blank=True, verbose_name="Додаткова інформація")
    role = models.ForeignKey(RoleUser, verbose_name="Роль користувача", on_delete=models.CASCADE, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'
        ordering = ['email']

