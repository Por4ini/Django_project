from django.db import models

class CommunityHromady(models.Model):
    code = models.TextField()
    code_old = models.TextField()
    locality = models.TextField()
    type = models.TextField()
    district = models.TextField()
    region = models.TextField()
    maps = models.TextField()
    all_data = models.TextField()
    all_attribute = models.TextField()
    center = models.TextField()
    registration = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'community_hromady'
