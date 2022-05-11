from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
   path('', views.Registration, name="Registration"),
   path('Login',views.Login,name="Login"),


]