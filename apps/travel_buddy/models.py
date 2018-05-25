from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
from datetime import datetime, date
import re

class UserManager(models.Manager):
    def validate(self, request):
        valid = True
        if request.method != "POST":
            valid = False
        for key in request.POST:
            if len(request.POST[key]) < 2:
                valid = False
                messages.error(request, "Each field needs to at least be 2 characters, (8 for Password)")
        if request.POST["pass1"] != request.POST["pass2"]:
            valid = False
            messages.error(request, "Passwords must match")
        if len(request.POST["pass1"]) < 8:
            valid = False
            messages.error(request, "Password must be at least 8 characters")
        return valid

class TripManager(models.Manager):
    def validate(self, request):
        valid = True
        if request.method != "POST":
            valid = False
        for key in request.POST:
            if request.POST[key] == "":
                valid = False
                messages.error(request, "Fields cannot be blank")
        if request.POST["tstartdate"] == "" or request.POST["tenddate"] == "":
            messages.error(request, "Date fields cannot be blank!")
            valid = False
        else:
            current_day = datetime.today()
            start = datetime.strptime(request.POST["tstartdate"], '%Y-%m-%d')
            end = datetime.strptime(request.POST["tenddate"], '%Y-%m-%d') 
            if start < current_day:
                valid = False
                messages.error(request, "Please ensure date fields are set for future date (not today)")
            if end < start:
                valid = False
                messages.error(request, "Please make sure dates are correct")
        return valid

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Trip(models.Model):
    tripname = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    tstartdate = models.DateField()
    tenddate = models.DateField()
    created_by = models.ForeignKey(User, related_name="trips")
    created_at = models.DateTimeField(auto_now_add=True)
    objects = TripManager()

class JoinedTrips(models.Model):
    user = models.ForeignKey(User, related_name="joinedtrip")
    trip = models.ForeignKey(Trip, related_name="joinedtrip")
    created_at = models.DateTimeField(auto_now_add=True)