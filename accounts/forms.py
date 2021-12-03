from django import forms
from .models import Account


class RegistrationForm(forms.ModelForm):



    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'password']

    
    def __init(self, *args, **kwargs): 
        super(RegistrationForm, self).__init__(*args, **kwargs)

        for field in self.fields: 
            self.fields[field].widget.attrs['class'] = ''