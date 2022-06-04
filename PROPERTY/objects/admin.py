from django.contrib import admin
from .models import Object


class ObjectsAdmin(admin.ModelAdmin):
    list_display = ("address", "title", "components", "share_size", "total_area", "location", "image", "documents", 'community')

admin.site.register(Object)