from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

# Create your views here.
def about(request):
    return render(request,'about.html')

    
