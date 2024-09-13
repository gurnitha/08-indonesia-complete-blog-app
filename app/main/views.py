# app/main/views.py

# Django and third modules
from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def halo_dunia(request):
    now = datetime.datetime.now()
    html = "<html><body>Halo Dunia!<br> Ini adalah waktu Bojonggede, Bogor (Jakarta) %s.</body></html>" % now
    return HttpResponse(html)