"""This module handles urls for the Users app."""
from django.urls import path
from . import views

app_name = "Users"

urlpatterns = [
    path('login/', views.user_login, name="user_login"),
    path('signup/', views.user_signup, name="user_signup"),
    path('logout/', views.user_logout, name='user_logout'),
]