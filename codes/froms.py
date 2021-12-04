from django import forms
from django.forms import fields
from .models import VerificationCode



class CodeForm(forms.ModelForm):

    number = forms.CharField(label="کد تایید پیامکی", help_text='کد ارسال شده پنج رقمی به شماره همراهتان را وارد کنید.')

    class Meta: 
        model = VerificationCode
        fields = ("number",)

    