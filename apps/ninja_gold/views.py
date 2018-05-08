# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from datetime import datetime
import random

def index(request):
    if "gold" not in request.session:
        request.session["gold"] = 0
    if "events" not in request.session:
        request.session["events"] = []
    return render(request, 'ninja_gold/index.html/')

def process_gold(request):
    print request.POST["building"]
    location = request.POST["building"]
    if location == 'cave':
        new_gold = random.randrange(5, 10)
        request.session['gold'] += new_gold
        request.session['events'].append(log_event(new_gold, 'cave'))
    elif location == 'house':
        new_gold = random.randrange(2, 5)
        request.session['gold'] += new_gold
        request.session['events'].append(log_event(new_gold, 'house'))
    elif location == 'farm':
        new_gold = random.randrange(10, 20)
        request.session['gold'] += new_gold
        request.session['events'].append(log_event(new_gold, 'farm'))
    elif location == 'casino':
        new_gold = random.randint(-50, 50)
        request.session['gold'] += new_gold
        request.session['events'].append(log_event(new_gold, 'casino'))
    return redirect('/ninja_gold/')

def clear(request):
    request.session.clear()
    return redirect('/')

def log_event(gold, location):
    now = datetime.now()
    if gold > 0:
        event_string = 'Earned '+ str(gold) +' golds from the '+ str(location) +'! ('+ str(now) +')'
    else:
        event_string = 'Entered a casino and lost '+ str(gold) +'...Ouch.. ! ('+ str(now) +')'
    return event_string