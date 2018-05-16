# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.TextField()
    state = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Ninja(models.Model):
    dojo_id = models.ForeignKey(Dojo, related_name="ninjas")
    f_name = models.CharField(max_length=255, default='0000000')
    l_name = models.CharField(max_length=255, default='0000000')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    