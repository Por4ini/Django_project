from django.contrib import admin
from .models import Subjects, SubjectDocuments, SubjectImages


class SubjectsAdmin(admin.ModelAdmin):
    list_display = ("title", "object", 'status', "balance_holder", "components", "part_size", "area", "period_of_use")
    search_fields = ("title",)


class SubjectDocumentsAdmin(admin.ModelAdmin):
    list_display = ['title', 'documents', 'subject']
    search_fields = ("title", "subject")


class SubjectImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'image','subject']
    search_fields = ("title", 'subject')


admin.site.register(Subjects, SubjectsAdmin)
admin.site.register(SubjectDocuments, SubjectDocumentsAdmin)
admin.site.register(SubjectImages, SubjectImagesAdmin)
