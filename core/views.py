# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def index(request):
    context = {
        'title': 'PostMan'
    }
    return render(request, 'index.html', context)