from django import forms
from .models import Account


class RegistrationForm(forms.ModelForm):

    password = forms.CharField(widget= forms.PasswordInput(attrs= {
     
        "type" : "password"
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'password']


    def clean(self): 
        clean_data = super(RegistrationForm, self).clean()

        phone_number = clean_data.get('phone_number')

        if(len(phone_number) != 11) : 
            raise forms.ValidationError(
                "شماره تلفن همراه باید 11 رقمی باشد."
            )
    
    def __init(self, *args, **kwargs): 
        super(RegistrationForm, self).__init__(*args, **kwargs)

        for field in self.fields: 
            self.fields[field].widget.attrs['class'] = ''