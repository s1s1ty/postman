# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.shortcuts import render, redirect
from django.contrib import messages

from account.models import Profile
from .forms import SendProductForm


def index(request):
    context = {
        'title': 'PostMan'
    }
    return render(request, 'index.html', context)


def view_qr_code(request):
    import pdb; pdb.set_trace()
    context = {
        'code': 'qrcode'
    }
    return render(request, 'add_send_product.html', context)


def send_product_add(request):
    form = SendProductForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            data_dict = instance.__dict__
            print data_dict
            saved_list = []
            saved_list.append(instance)
            request.session['saved'] = saved_list
            return redirect('/qr-code/')

        else:
            messages.error(request, "Form is not valid")

    context = {
        'form': form,
        'headline': 'Delivery Item'
    }
    return render(request, 'add_send_product.html', context)