from django.contrib import admin
from .models import Event
from django.contrib.admin import ModelAdmin

class EventAdmin(ModelAdmin):
    list_display = ('title', 'created_at')
    list_display_links = ('title', 'created_at')
    readonly_fields = ('created_at',)
    ordering = ('created_at',)

    
    list_filter = ('created_at',)
    search_fields = ('title','description')
    

admin.site.register(Event, EventAdmin)