from __future__ import unicode_literals
import datetime, re, bcrypt
from django.contrib import messages
from django.shortcuts import redirect, render
from models import Auser

def index(request):
    return render(request, 'log_reg_dj/index.html')

def register(request):
    hash1 = bcrypt.hashpw(request.POST["pass1"].encode(), bcrypt.gensalt())
    hash2 = bcrypt.hashpw(request.POST["pass2"].encode(), bcrypt.gensalt())
    data = {
        "fname" : request.POST["fname"],
        "lname" : request.POST["lname"],
        "email" : request.POST["email"],
        "pass1" : hash1,
        "pass2" : hash2,
        "created_at" : str(datetime.date.today()),
    }
    if validate(data):
        Auser.objects.create(first_name=data["fname"],last_name=data["lname"],email=data["email"],password=data["pass1"], created_at=data["created_at"])
    else:
        messages.error(request, messages.INFO, "Please fix all errors")
    return redirect('/log_reg_dj/')

def login(request):
    data = {
        "email" : request.POST["email"],
        "pass" : request.POST["pass"]
    }
    users = Auser.objects.filter(email = data["email"])
    if len(users) > 0:
        match_user = users[0] 
        if bcrypt.checkpw(data["pass"].encode(), match_user.password.encode()):
            request.session["id"] = match_user.id
            request.session["user"] = match_user.first_name+" "+match_user.last_name
            return render(request, 'log_reg_dj/success.html')
        else:
            messages.error(request, messages.INFO, "Password not correct!")
    else:
        messages.error(request, messages.INFO, "That email is not registered")
    return redirect('/log_reg_dj/')

def validate(d):
    valid = True
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if len(d["fname"]) < 2:
        valid = False
        messages.add_message(request, messages.INFO, "Name must be < 2")
    if len(d["lname"]) < 2:
        valid = False
        messages.add_message(request, messages.INFO, "Name must be < 2")
    if str(d["pass1"]) == str(d["pass2"]):
        valid = False
        messages.add_message(request, messages.INFO, "Please match passwords")
    if not EMAIL_REGEX.match(d["email"]):
        valid = False
        messages.add_message(request, message.INFO, "Please enter a valid email")
    return valid