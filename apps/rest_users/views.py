from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
import datetime

def index(request):
    return render(request, 'index.html')

def new(request):
    return render(request, 'add.html')

def edit(request, id):
    request.session["edit"] = []
    for x in request.session["users"]:
        if int(x["id"]) == int(id):
            request.session["edit"] = x
    request.session.modified = True
    return render(request, 'edit.html')

def show(request, id):
    request.session["show"] = []
    for x in request.session["users"]:
        if int(x["id"]) == int(id):
            request.session["show"] = x
    request.session.modified = True
    return render(request, 'show.html')

def create(request):
    user_id = len(request.session["users"]) + 1
    data = { 
        "id": user_id,
        "fname": request.POST["fname"],
        "lname": request.POST["lname"],
        "email": request.POST["email"],
        "created_at" : str(datetime.date.today()),
    }
    request.session["users"].append(data)
    request.session["user_count"] += 1
    request.session.modified = True
    return redirect('/rest_users/users/')

def destory(request, id):
    s = request.session["users"]
    for x in range(len(s)):
        if int(s[x]['id']) == int(id):
            del s[x]
            break

    request.session["users"] = s
    request.session.modified = True
    return redirect("/rest_users/users/")

def update(request):
    s = request.session["users"]
    match_id = int(request.POST["id"])
    for x in range(len(s)):
        if int(s[x]["id"]) == match_id:
            data = {
                "id" : s[x]["id"],
                "fname" : request.POST["fname"],
                "lname" : request.POST["lname"],
                "email" : request.POST["email"],
                "created_at" : s[x]["created_at"] 
            }
            s[x] = data
    request.session["users"] = s
    request.session.modified = True
    return redirect('/rest_users/users/')