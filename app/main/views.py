# app/main/views.py

# Django and third modules
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def halo_dunia(request):
    html = "Halo Dunia!<br> dari Bojonggede, Bogor"
    return HttpResponse(html)