from django.contrib.auth.models import models


class CommunityHromady(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    code = models.CharField(max_length=120)
    code_old = models.CharField(max_length=120)
    locality = models.CharField(max_length=120)
    type = models.CharField(max_length=120)
    district = models.CharField(max_length=120)
    region = models.CharField(max_length=120)
    maps = models.TextField(max_length=None)
    all_data = models.TextField(blank=True)
    all_attribute = models.TextField(blank=True)
    center = models.TextField(blank=True)
    registration = models.IntegerField()
    flag = models.ImageField(blank=True, verbose_name='прапор')
    emblem = models.ImageField(blank=True, verbose_name="Герб")

    class Meta:
        managed = True
        db_table = 'community_hromady'
        verbose_name = 'Громада'
        verbose_name_plural = 'Громади'

    def __str__(self):
        title = '{0.locality} {0.type} {0.district} {0.region}'
        return title.format(self)


class Advertisement(models.Model):
    title_advertisement = models.CharField(max_length=120, verbose_name='Заголовок')
    advertisement = models.CharField(max_length=1000, verbose_name='Текст оголошення')
    image_advertisement = models.ImageField(verbose_name='Зображення')
    created_at = models.DateField(auto_now_add=True)
    community = models.ForeignKey(CommunityHromady, verbose_name="Громада", on_delete=models.CASCADE, default=1)

    class Meta:
        managed = True
        verbose_name = 'Оголошення'
        verbose_name_plural = 'Оголошення'

    def __str__(self):

        return self.title_advertisement
