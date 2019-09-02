from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render, redirect

urlpatterns=[
    path('',views.index, name='index'),
    path('explore',views.explore,name ='explore'),
    path('notification',views.notification,name ='notification'),
    path('profile',views.profile,name ='profile'),
    path('logout',views.index,{'next_page': 'accounts:login'}, name='logout'),
    path('upload',views.upload,name ='upload'),
]



