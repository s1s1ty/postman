# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render, redirect
from django.contrib import messages

from account.models import Profile
from core.models import SendProduct
from .forms import SendProductForm


def index(request):
    context = {
        'title': 'PostMan'
    }
    return render(request, 'index.html', context)


def view_qr_code(request):
    data_dict = request.session.get('saved')
    del data_dict['csrfmiddlewaretoken']
    instance = SendProduct(**data_dict)
    instance.user = Profile.objects.get(user_id=request.user)
    img_name = instance.generate_qrcode
    print img_name
    if request.POST:
        # import pdb;pdb.set_trace()
        instance.save()
        messages.success(request, "Product Delivery Successful")
    context = {
        'code': 'qrcode',
        'img': img_name
    }
    return render(request, 'add_send_product.html', context)


def send_product_add(request):
    form = SendProductForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            request.session['saved'] = request.POST
            return redirect('/qr-code/')

        else:
            messages.error(request, "Form is not valid")

    context = {
        'form': form,
        'headline': 'Delivery Item'
    }
    return render(request, 'add_send_product.html', context)