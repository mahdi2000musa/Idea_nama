
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError


class MyAccountManager(BaseUserManager) :
    def create_user(self, first_name, last_name, phone_number, password = None, ):

        if not phone_number: 
            raise ValidationError('برای ثبت نام شماره همراه راوارد کنید')

        if not first_name or not last_name: 
            raise ValidationError('نام و نام خانوادگی را به طور کامل و صحیح وارد کنید')

        user = self.model(
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number,
            username = None
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, first_name, last_name, phone_number, password):

        user = self.create_user(
            first_name= first_name,
            last_name = last_name,
            phone_number= phone_number,
            password= password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True

        user.save(using = self._db)
    

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=191,)

    #required

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now= True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)


    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MyAccountManager()

    def __str__(self): 
        return self.phone_number

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True

    

    


