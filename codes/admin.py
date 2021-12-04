from django.contrib import admin
from .models import VerificationCode


class CodeAdmin(admin.ModelAdmin): 
    readonly_fields= ("number", "user")

admin.site.register(VerificationCode, CodeAdmin)
