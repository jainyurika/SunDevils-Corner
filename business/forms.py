from django import forms
from django.forms import ModelForm, widgets
from .models import Business

class BusinessForm(ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'about', 'phone', 'address', 'website', 'distfromcampus']
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'register-form-field', 'placeholder': 'Name'}),
            'about' : forms.Textarea(attrs={'class': 'register-form-field', 'placeholder': 'About'}),
            'phone' : forms.TextInput(attrs={'class': 'register-form-field', 'placeholder': 'Phone'}),
            'address' : forms.TextInput(attrs={'class': 'register-form-field', 'placeholder': 'Address'}),
            'website' : forms.TextInput(attrs={'class': 'register-form-field', 'placeholder': 'Website'}),
            'distfromcampus' : forms.TextInput(attrs={'class': 'register-form-field', 'placeholder': 'Distance From Campus'}),
        }