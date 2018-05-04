# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    s = request.session
    if "count" not in s:
        s["count"] = 1
    if "randword" not in s:
        s["randword"] = get_random_string(length=32)
    if request.method == "POST":
        s["randword"] = get_random_string(length=32)
        s["count"] += 1
    data = {
        "id": s["randword"],
        "count": s["count"]
    }
    return render(request, 'rand_word/index.html', data)