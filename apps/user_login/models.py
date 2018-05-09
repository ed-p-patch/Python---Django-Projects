# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    e_addr = models.TextField()
    u_age = models.IntegerField()
    c_time = models.DateTimeField(auto_now_add = True)
    u_time = models.DateTimeField(auto_now = True)