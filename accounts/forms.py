from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Account
from django.contrib.admin.widgets import AdminDateWidget

class SignUpForm(UserCreationForm):
    GENDER_OPTIONS = [
        ('None', 'Select Value'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    CLASSSTANDING_OPTIONS = [
        ('None', 'Select Value'),
        ('Freshman', 'Freshman'),
        ('Sophomore', 'Sophomore'),
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
        ('Graduate', 'Graduate'),
    ]

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    dob = forms.DateField(input_formats=['%d/%m/%Y'], required=False,widget=AdminDateWidget(attrs={'class': 'form-control', 'placeholder': 'Date of Birth'}))
    gender = forms.ChoiceField(choices=GENDER_OPTIONS, required=True, widget=forms.Select(attrs={'class':'form-control'}))
    classstandings = forms.ChoiceField(choices=CLASSSTANDING_OPTIONS, required=True, widget=forms.Select(attrs={'class':'form-control'}))
    # major = forms.CharField()
    
    class Meta(UserCreationForm.Meta):
        model = Account
        fields = ['fname', 'lname', 'email', 'dob', 'gender', 'classstandings', 'major', 'password1', 'password2']
        widgets = {
            'fname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'lname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),    
            # 'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'major': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Major'}),
            }

    def clean_email(self):
        email = self.cleaned_data['email']
        domain = email.split("@")[1]
        if domain != "asu.edu":
            raise forms.ValidationError("Not an @asu.edu email. Enter a valid email.")
        return email
    
    # def clean_email(self):
    #     data = self.cleaned_data['email']
    #     data = data + "asu.edu"
    #     return data
    
    # def save(self, commit=True):
    #     user = super(SignUpForm, self).save(commit=False)
    #     user.email = self.cleaned_data["email"]
    #     if commit:
    #         user.save()
    #     return user
    # @transaction.atomic
    # def save(self):
    #     user = super().save(commit=False)
    #     user.save()
    #     # udept = UserDepartment.objects.create(user=user)
    #     return user

#forms.DateField(attrs={'class': 'form-control', 'placeholder': 'Date of Birth'})