# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model

from .forms import UserForm, ProfileForm, LoginForm


def generate_password():
    pass


def generate_username():
    pass


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

            user_login = user.authenticate(username=username, password=password)
            if user_login is not None:
                if user_login.is_active:
                    login(request, user_login)
                    return redirect('/')

    context = {
        'title': 'Registration',
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'form.html', context)


def login_view(request):
    login_form = LoginForm(request.POST or None)
    if request.method == 'POST':
        username = login_form.cleaned_data['username']
        password = login_form.cleaned_data['password']
        user = login_form.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return render('/')

    context = {
        'title': 'Login',
        'form': login_form
    }
    return render(request, 'form.html', context)


def logout_view(request):
    logout(request)
    return redirect("/")