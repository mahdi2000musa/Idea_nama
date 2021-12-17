from django.db import models
from ckeditor.fields import RichTextField 
from django_jalali.db import models as jmodels


class Event(models.Model) :

    title = models.CharField(max_length=191, blank=False, verbose_name='تیتر خبر')
    description = RichTextField(verbose_name='متن خبر')
    image = models.ImageField(upload_to = 'event_image', blank=  True, verbose_name='تصویر خبر')
    file=  models.FileField(upload_to="event_form", blank=True, verbose_name='فرم ها')
    created_at= jmodels.jDateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')


    def __str__(self) :
        return self.title

    class Meta:
        verbose_name = "رویداد ها"
        verbose_name_plural = 'رویداد ها'
