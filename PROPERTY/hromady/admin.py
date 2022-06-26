from django.contrib import admin
from .models import CommunityHromady, Advertisement


class CommunityAdmin(admin.ModelAdmin):
    list_display = ("code", "code_old", "locality", "type", "district", "region", "all_data", "all_attribute", "center", "registration", "flag", "emblem")
    search_fields = ("code", "locality")

class AdvertisementAdmin(admin.ModelAdmin):
    model = Advertisement
    list_display = ("title_advertisement", "advertisement", "image_advertisement", "created_at")


admin.site.register(CommunityHromady, CommunityAdmin)
admin.site.register(Advertisement, AdvertisementAdmin)
