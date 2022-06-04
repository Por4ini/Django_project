from django.contrib.auth.models import  AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from hromady.models import CommunityHromady
from .manager import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    community = models.ForeignKey(CommunityHromady, verbose_name="Громада", on_delete=models.CASCADE, default=1)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email