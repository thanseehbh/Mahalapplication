from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from mypageapp import views

app_name = 'mypageapp'

urlpatterns = [
    path('', views.index,name='index'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('mahal_page/', views.mahal_page, name='mahal_page'),
    path('mahal_reg/', views.mahal_reg, name='mahal_reg'),
    path('user_profile_reg/', views.user_profile_reg, name='user_profile_reg'),
    ]
