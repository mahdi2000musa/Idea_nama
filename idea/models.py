from django.db import models
from accounts.models import Account
from django_jalali.db import models as jmodles

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, blank=False)
    category_desc = models.CharField(max_length=191, blank=False)
    category_img = models.ImageField(upload_to='category_image/',blank =True)
    
    def __str__(self):
        return f'{self.category_name}'



class Idea_Bank(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=191, blank=False)
    desc = models.TextField(max_length=3000, )
    contact = models.CharField(max_length=150, blank=False)
    comp_file = models.FileField(blank=True, upload_to='idea_file/')
    score = models.IntegerField(default = 0 , blank=True)
    created_at = jmodles.jDateTimeField(auto_now_add=True)
    updated_at = jmodles.jDateTimeField(auto_now=True)
    like = models.IntegerField(default=0,)
    is_accepted = models.BooleanField(default=False)
    category = models.ForeignKey(Category, verbose_name="دسته بندی", on_delete=models.CASCADE)
    participant_place = models.CharField(max_length=191, blank= False, default = "")
    can_edit = models.BooleanField(default=False)

   
    
    def __str__(self):
        return self.title




