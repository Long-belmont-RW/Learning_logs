"""Defines the url path for users"""
from django.urls import path, include
from . import views
app_name = 'users'
urlpatterns = [
    #Include defaul auth urls.
    path('', include('django.contrib.auth.urls')),
    #Registration page
    path('register/', views.register, name='register')
]
