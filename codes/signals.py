from django.contrib.auth.models import User
from accounts.models import Account
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import VerificationCode


@receiver(post_save, sender=Account)
def post_save_generate_code(sender, instance, created, *args, **kwargs): 

    if created: 
        VerificationCode.objects.create(user = instance)  