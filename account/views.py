# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate, get_user_model

from .forms import UserForm, ProfileForm


def registration(request):
    user_form = UserForm(request.POST or None)
    profile_form = ProfileForm(request.POST or None)

    if request.method == 'POST':
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)

            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']

            user.set_password(password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user_id = user
            profile.save()

    context = {
        'title': 'Registration',
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'form.html', context)


def login(request):
    context = {
        'title': 'Login'
    }
    return render(request, 'form.html', context)


def logout(request):
    context = {
        'title': 'Logout'
    }
    return render(request, '', context)
