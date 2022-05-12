from socket import fromshare
from django import forms
from .models import Dog

class NewDogForm(forms.ModelForm):
        class Meta:
            model = Dog
            fields = ['name', 'breed']

class AdoptDogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ['owner']
        widgets = {'owner': forms.HiddenInput()}
