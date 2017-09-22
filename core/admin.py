# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import SendProduct


class SendProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'item_name', 'delivery_address', 'payment_type', 'payable_amount', 'delivery_charge']
    readonly_fields = ['user', 'item_name', 'item_details', 'delivery_address',
                       'payment_type', 'payable_amount', 'delivery_charge', 'qr_code']

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(SendProduct, SendProductAdmin)
admin.site.disable_action('delete_selected')
