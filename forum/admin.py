from django.contrib import admin

from django.contrib import admin
from .models import Category, Topic, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


class TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'category','user','update_at']
    search_fields = ("title",)


class PostAdmin(admin.ModelAdmin):
    list_display = ['text', 'topic', 'user', 'created_at']
    search_fields = ("text",)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)
