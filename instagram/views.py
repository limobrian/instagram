# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    all_images = Image.objects.all()
    all_users = Profile.objects.all()
    next = request.GET.get('next')
    if next: return redirect(next)
    return render(request, 'display/home.html',  {"all_images": all_images}, {"all_users":all_users})


@login_required(login_url='/accounts/login/')
def explore(request):
    return render(request, 'display/explore.html')

@login_required(login_url='/accounts/login/')
def notification(request):
    return render(request, 'display/notification.html')



