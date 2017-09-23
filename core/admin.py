# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import SendProduct


def update_delivery_status(modeladmin, request, queryset):
    for item in queryset:
        item.delivery_status = 1
        item.save()


def update_paid_status(modeladmin, request, queryset):
    for item in queryset:
        item.paid = 1
        item.save()


update_delivery_status.short_description = 'Delivery Successful'
update_paid_status.short_description = 'Paid Successful'


class SendProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'item_name', 'delivery_address',
                    'payment_type', 'payable_amount',
                    'delivery_charge', 'paid', 'delivery_status']

    readonly_fields = ['user', 'item_name', 'item_details', 'delivery_address',
                       'payment_type', 'payable_amount', 'delivery_charge', 'qr_code']

    search_fields = ['user', 'paid', 'delivery_status']

    actions = [update_delivery_status, update_paid_status]

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(SendProduct, SendProductAdmin)
admin.site.disable_action('delete_selected')
