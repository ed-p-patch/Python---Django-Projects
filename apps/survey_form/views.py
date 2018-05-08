# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    return render(request, 'survey_form/index.html')

def process(request):
    s = request.session
    if "count" not in s:
        s["count"] = 1
    data = { 
        "name": request.POST["name"],
        "location": request.POST["location"],
        "language": request.POST["language"],
        "comment": request.POST["comment"]
    }
    s["count"] += 1
    messages.add_message(request, messages.INFO, 'Thanks for submitting this form!\n You have submitted this form {} times.'.format(s["count"]))
    return render(request, 'survey_form/result.html', data)