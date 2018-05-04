# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    time = {
         "server_time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request, 'time_display/templates/index.html', time)