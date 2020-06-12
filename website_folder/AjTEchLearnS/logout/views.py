from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# Create your views here.


def handlelogout(request):
    auth.logout(request)
    # messages.success(request,"Successfully logged Out")
    return redirect('home')