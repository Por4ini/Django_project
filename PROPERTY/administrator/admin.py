from django.contrib import admin
from .models import Contacts


class ContactsAdmin(admin.ModelAdmin):
    list_display = ("name", 'role', 'phone', 'messenger', 'hromada')
    search_fields = ("title",)


admin.site.register(Contacts, ContactsAdmin)

