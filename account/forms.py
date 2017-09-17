from django import forms
from django.contrib.auth.models import User

from .models import Profile


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Choose a username'
        }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder':'Create a password'
        }))

    class Meta:
        model = User
        fields = ['username', 'password']


class ProfileForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Fullname'
        }))

    present_address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your present Address'
        }))

    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Email Address'
        }))

    class Meta:
        model = Profile
        fields = ('user_type','full_name', 'present_address', 'email')


class ProfileUpdateForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        }))
    company_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        }))
    office_address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        }))
    present_address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        }))
    permanent_address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        }))
    website = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        }))
    facebook_page = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        }))
    class Meta:
        model = Profile
        exclude = ('user_id', 'user_type')
        fields = '__all__'
            
        

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
        }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Put Password'
        }))

