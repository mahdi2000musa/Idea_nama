from django.db import models
from django.db.models import fields
from accounts.models import Account
from django_jalali.db import models as jmodles

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, blank=False, verbose_name='نام دسته بندی')
    category_desc = models.CharField(max_length=191, blank=False, verbose_name='موضوع دسته بندی')
    category_img = models.ImageField(upload_to='category_image/',blank =True, verbose_name='عکس دسته بندی')
    
    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'موضوع رویداد ها'
        verbose_name_plural = 'موضوع رویداد ها'




class Idea_Bank(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='کاربر')
    title = models.CharField(max_length=191, blank=False, verbose_name='موضوع')
    desc = models.TextField(verbose_name='چکیده')
    contact = models.CharField(max_length=150, blank=False, verbose_name='مخاطبان')
    comp_file = models.FileField(blank=True, upload_to='idea_file/', verbose_name='فرم بارگزاری شده')
    score = models.IntegerField(default = 0 , blank=True, verbose_name='امتیاز')
    created_at = jmodles.jDateTimeField(auto_now_add=True, verbose_name='ایجاد شده')
    updated_at = jmodles.jDateTimeField(auto_now=True, verbose_name='ویرایش شده')
    like = models.IntegerField(default=0, verbose_name='تعداد علاقه مندی')
    is_accepted = models.BooleanField(default=False, verbose_name='تایید ضده')
    category = models.ForeignKey(Category, verbose_name="دسته بندی", on_delete=models.CASCADE)
    participant_place = models.CharField(max_length=191, blank= False, default = "", verbose_name='محل برگزاری')
    can_edit = models.BooleanField(default=False, verbose_name='امکان ویرایش')

   
    
    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'بانک ایده ها'
        verbose_name_plural = 'بانک ایده ها'




