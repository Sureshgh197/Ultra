from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('up/',views.upload_Image),
    path('accounts/',views.accounts_register),
    path('accounts/register/',views.register),
    path('success',views.success),
    path('login/',views.custom_login),
    path('logout/',views.logout),
    path('<str:uname>/',views.profile)
    
]
