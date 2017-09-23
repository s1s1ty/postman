# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F
from django.shortcuts import render, redirect
from django.contrib import messages

from core.models import SendProduct
from .forms import SendProductForm


def index(request):
    context = {
        'title': 'PostMan'
    }
    return render(request, 'index.html', context)


@login_required
def view_qr_code(request):
    data_dict = request.session.get('saved')
    del data_dict['csrfmiddlewaretoken']
    instance = SendProduct(**data_dict)
    instance.user = request.user
    img_name = instance.generate_qrcode
    print img_name
    if request.POST:
        # import pdb;pdb.set_trace()
        # instance.save()
        messages.success(request, "Successfully sent your product for delivery")
    context = {
        'code': 'qrcode',
        'img': img_name
    }
    return render(request, 'add_send_product.html', context)


@login_required
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


@login_required
def product_list(request):
    query = SendProduct.objects.filter(user=request.user)
    total_taka = query.aggregate(total=Sum(F('payable_amount') + F('delivery_charge')))
    paid = query.filter(paid=1).aggregate(paid=Sum(F('payable_amount') + F('delivery_charge')))
    print total_taka
    context = {
        'title': 'My Product',
        'product': query,
        'total_taka': total_taka.get('total'),
        'paid': paid.get('paid') if paid.get('paid') else 0,
        'due': (total_taka.get('total') - paid.get('paid')) if paid.get('paid') else total_taka.get('total')
    }
    return render(request, 'product_list.html', context)