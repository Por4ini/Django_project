from django.db import models
from user.models import CustomUser


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Категорія')

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.title


class Topic(models.Model):
    title = models.CharField(max_length=50, verbose_name='Тема')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    update_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата оновлення', blank=True, null=True)

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Теми'
    def __str__(self):
        return self.title

class Post(models.Model):
    text = models.CharField(max_length=5000, verbose_name='Пост')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дати дотавання')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)


    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пости'
        ordering = ['-id']
    def __str__(self):
        return 'Пост'