"""
URL configuration for TrackMyCash project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
"""


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("accounts.urls")),
    path('admin/', admin.site.urls),
]