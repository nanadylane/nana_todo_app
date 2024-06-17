from .models import *
from django import forms

from django.forms import (
    DateInput,     
)

from django.contrib.auth.forms import UserCreationForm
class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2'] 
class NanaTaskForm(forms.ModelForm):
    
    class Meta:
        model = NanaTask
        # fields = '__all__'
        exclude = ('owner',)
        widgets = {
            'due_date': DateInput(attrs = {
                'type':'date'
            }),
          }

class NanaTagForm(forms.ModelForm):
    
    class Meta:
        model = NanaTag
        fields = '__all__'
       
