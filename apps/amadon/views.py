# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if "total" not in request.session:
        request.session["total"] = 0
    if "last-purchase" not in request.session:
        request.session["last-purchase"] = ""
    if "num_items" not in request.session:
        request.session["num_items"] = 0
    return render(request, 'amadon/index.html')

def buy(request):
    data = {
        "q": int(request.POST["quantity"]),
        "id": request.POST["product_id"],
        "cart": getprice(int(request.POST["quantity"]), int(request.POST['product_id']))
    }
    request.session["num_items"] += data["q"]
    request.session["total"] += data["cart"]
    request.session["cart"] = data["cart"]
    return redirect('/amadon/checkout/')

def checkout(request):
    return render(request, 'amadon/checkout.html')
def clear(request):
    request.session.clear()
    return redirect('/amadon/')

def getprice(q, id):
    price = 0
    if id == 1015:
        print "shirt"
        price = 19.99
    elif id == 1016:
        print "sweater"
        price = 29.99
    elif id == 1017:
        print "mug"
        price = 4.99
    elif id == 1018:
        print "book"
        price = 49.99
    return q * price