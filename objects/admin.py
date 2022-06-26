from django.contrib import admin
from .models import Object, ObjectImages, ObjectDocuments


class ObjectsAdmin(admin.ModelAdmin):
    list_display = ("title", "components", "hromada", "share_size", "total_area", "location")
    search_fields = ("title",)


class ObjectImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'object']
    search_fields = ("title", "object")


class ObjectDocumentsAdmin(admin.ModelAdmin):
    list_display = ['title', 'documents', 'object']
    search_fields = ("title", "object")


admin.site.register(Object, ObjectsAdmin)
admin.site.register(ObjectDocuments, ObjectDocumentsAdmin)
admin.site.register(ObjectImages, ObjectImagesAdmin)
