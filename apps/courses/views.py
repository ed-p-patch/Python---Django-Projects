from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
import datetime

def index(request):
    if "courses" not in request.session:
        request.session["courses"] = []
    request.session.modified = True
    return render(request, "courses/index.html")

def create(request):
    if validate(len(request.POST["name"]), len(request.POST["description"]), request):
        c_id = len(request.session["courses"]) + 1
        data = {
            "name": request.POST["name"],
            "description": request.POST["description"],
            "created_at": str(datetime.date.today()),
            "id": c_id,
        }
        request.session["courses"].append(data)
        request.session["num_courses"] += 1
        request.session.modified = True
    else:
        messages.add_message(request, messages.INFO, "Please fix the above errors")
    request.session.modified = True
    return redirect('/courses/courses/')

def show_delete(request, id):
    request.session["stage_delete"] = []
    s = request.session["courses"]
    for x in range(len(s)):
        if int(s[x]["id"]) == int(id):
            request.session["stage_delete"] = s[x]
    request.session.modified = True
    return render(request, 'courses/destroy.html')

def delete_item(request, id):
    s = request.session["courses"]
    for x in range(len(s)):
        if int(s[x]['id']) == int(id):
            del s[x]
            break
    request.session.modified = True
    return redirect('/courses/courses/')
    
def validate(a, b, request):
    valid = True
    if a < 6:
        messages.add_message(request, messages.INFO, "Course name must be greater than 5 characters")
        valid = False
    if b < 16:
        messages.add_message(request, messages.INFO, "Description must be greater than 15 characters")
        valid = False
    return valid