# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from datetime import datetime

def index(request):
    s = request.session
    if "words" not in s:
        s["words"] = []
    return render(request, 'session_words/index.html')

def add(request):    
    new_word = {
        "text": request.POST["word"],
        "color": request.POST["color"],
        "added": datetime.strftime(datetime.now(),  "%H:%M:%S %p, %B %d, %Y")
    }
    if 'big' not in request.POST:
        new_word["big"] = "regular"
    else:
        new_word["big"] = "big"
    request.session["words"].append(new_word)
    request.session.modified = True
    return redirect('/session_words/')

def clear(request):
    request.session.clear()
    return redirect('/session_words/')