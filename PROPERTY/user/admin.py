from django.contrib import admin
from .models import Profile


class ProfAdmin(admin.ModelAdmin):
    list_display = ("nickname", "position", "community", "avatar")
    search_fields = []


admin.site.register(Profile)
