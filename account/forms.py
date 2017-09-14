from django import forms
from django.contrib.auth.models import User

from .models import Profile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user_id',)
        fields = '__all__'


class LoginForm(forms.Form):
    USER_CHOICES = (
        ('M', 'Marchant'),
        ('U', 'User')
    )
    user_type = forms.ChoiceField(choices=USER_CHOICES)
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

