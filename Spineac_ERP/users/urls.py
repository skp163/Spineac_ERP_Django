from django.urls import path
from django.contrib import admin
from . import views

#/Users/sunilkumarpradhan/SpineacDigital/Spineac_ERP_Django/Spineac_ERP/users/views.py

urlpatterns = [
    path("", views.home),
]
