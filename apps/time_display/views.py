# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from time import gmtime, strftime
from django.shortcuts import render

def index(request):
    server_time = {
         "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    print server_time
    return render(request, 'time_display/index.html', server_time)