from django.shortcuts import render, redirect
from login.models import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login
from django.contrib import messages, auth
# Create your views here.
def login(request):
    if(request.method=="POST"):
        username=request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if(user is not None):
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('/OnlineExam/login/category/')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('/Center/login')
    else:
        return render(request , 'center/login.html')		

def addstudent(request):
    return render(request , 'center/addstudent.html')		
