# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate, get_user_model

from .forms import UserForm, ProfileForm, LoginForm
from .models import Profile

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

            user_login = authenticate(username=username, password=password)
            if user_login is not None:
                if user_login.is_active:
                    login(request, user_login)
                    return redirect('/')

    context = {
        'title': 'Registration',
        'user_form': user_form,
        'profile_form': profile_form,
        'flag': 'reg'
    }
    return render(request, 'form.html', context)


def login_view(request):
    login_form = LoginForm(request.POST or None)
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')
        user_exists = User.objects.filter(username=username).select_related('profile')


        if login_form.is_valid:
			user = authenticate(username=username, password=password)
			if user is not None and user.is_active:
				login(request, user)
				print user_type
				if user_type == 'M':
					return redirect('/')
				else:
					return redirect('/')

    context = {
        'title': 'Login',
        'form': login_form,
        'flag': 'login'
    }
    return render(request, 'form.html', context)


def profile_view(request, user_id):
    query = User.objects.filter(pk=user_id).select_related('profile')
    import pdb; pdb.set_trace()
    context = {
        'title': 'Profile',
        'info': query
    }
    return render(request, 'profile.html', context)
