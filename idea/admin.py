from django.contrib import admin
from .models import Category, Idea_Bank
from django.contrib.admin import ModelAdmin


class IdeaAdmin(ModelAdmin) :
    list_display = ["title", "contact" , "created_at", "category"]
    list_display_links = ["title", "contact" , "created_at", "category"]
    ordering = ['created_at',]

    list_filter = ('updated_at', 'created_at', 'is_accepted', 'can_edit','score', 'category')
    search_fields = ('title', 'desc', 'score')
    

admin.site.register(Idea_Bank, IdeaAdmin)
admin.site.register(Category)