from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'phone_number')
    list_display_links = ('first_name', 'last_name', 'phone_number')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        ('Personal info', {'fields': ('first_name', 'last_name', 'password', 'phone_number')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superadmin', 'is_admin')}),
    )
admin.site.register(Account, AccountAdmin)
