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

    class Meta:
        managed = True
        db_table = 'community_hromady'
