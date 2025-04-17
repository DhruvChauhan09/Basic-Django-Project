from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("login", views.login, name='login'),
    path("home", views.index, name='home'),
    path("settings", views.settings, name='settings'),
    path("contacts", views.contacts, name='contacts'),
    path("services", views.services, name='services'),
    path("about", views.about, name='about'),
]