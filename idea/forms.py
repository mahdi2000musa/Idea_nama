from django import forms
from django.contrib.auth.models import User 
from .models import Idea_Bank


class IdeaForm(forms.ModelForm): 

   
    
    class Meta: 
        model = Idea_Bank
        fields = ["title", "category", "desc","comp_file", "contact", "participant_place",]

    

    def __init__(self, *args, **kwargs):
        super(IdeaForm , self).__init__(*args, **kwargs)
        
        self.fields['title'].widget.attrs['placeholder'] = 'موضوع ر ا بنویسید.'
        self.fields['contact'].widget.attrs['placeholder'] = 'مخاطب'
        self.fields['category'].widget.attrs['placeholder'] = 'دسته بندی'
        self.fields['desc'].widget.attrs['placeholder'] = 'شرح مختصری از ایده خودرا بنویسید...'
        self.fields['participant_place'].widget.attrs['placeholder'] = 'محل اجرا'
        
        
        for field in self.fields: 
            self.fields[field].widget.attrs['class'] = 'form-control'