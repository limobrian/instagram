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

@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'display/userprofile.html')

def logout(request):
    return render(request, 'registration/logout.html')


def login(request):
    return render(request, 'registration/login.html')

@login_required(login_url='/accounts/login/')
def upload(request):
    current_user = request.user
    p = Profile.objects.filter(id=current_user.id).first()
    imageuploader_profile = Image.objects.filter(imageuploader_profile=p).all()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.imageuploader_profile= p
            post.save()
            return redirect('/')
    else:
        form =PostForm
    return render(request, 'display/upload.html', {"form": form})




