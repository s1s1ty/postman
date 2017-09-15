# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class DeliveryDetail(models.Model):
    PAYMENT_CHOICE = (
        ('A', 'Advanced'),
        ('C', 'COD'),
    )
    item_name = models.CharField(max_length=200)
    item_details = models.TextField()
    delivery_address = models.TextField()
    payment_type = models.CharField(max_length=1, choices=PAYMENT_CHOICE)
    payable_amount = models.IntegerField(default=0)
    delivery_charge = models.IntegerField(default=0)
    qr_code = models.ImageField(upload_to='qrcode', blank=True, null=True)



