# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    print "hey patrick"
    return render(request, 'survey_form/index.html')

def process(request):
    s = request.session
    if "count" not in s:
        s["count"] = 1
    data = {}
    print request.form["name"]
    return render(request, 'survey_form/result.html', data)