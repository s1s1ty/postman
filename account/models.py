# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.validators import URLValidator
from django.db import models


class Profile(models.Model):
    USER_CHOICES = (
        ('M', 'Marchant'),
        ('U', 'User')
    )
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    user_type = models.CharField(max_length=1, choices=USER_CHOICES)
    full_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=300, blank=True)
    office_address = models.TextField(blank=True)
    present_address = models.TextField()
    permanent_address = models.TextField(blank=True)
    email = models.EmailField()
    website = models.CharField(max_length=500, blank=True,validators=[URLValidator()])
    facebook_page = models.CharField(max_length=500, blank=True, validators=[URLValidator()])
    profile_pic = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return str(self.full_name)