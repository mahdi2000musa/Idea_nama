from django.contrib import admin
from .models import VerificationCode , SiteBanner


class CodeAdmin(admin.ModelAdmin): 
    readonly_fields= ("number", "user")

admin.site.register(VerificationCode, CodeAdmin)
admin.site.register(SiteBanner)
