# app/main/urls.py

# Django and third party modules
from django.urls import path

# Locals
from app.main import views 

# appname
app_name = 'main'

urlpatterns = [
    path("", views.halo_dunia, name='halo'),
]