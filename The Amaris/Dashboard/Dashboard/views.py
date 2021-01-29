from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import login as dj_login,logout as dj_logout,authenticate
from django.contrib import messages


def index(request):
    return render(request, 'index.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('Amaris')
    else:
        return render(request,"login.html")

def hanlogin(request):
    if request.user.is_authenticated:
        return redirect('Amaris')
    else:
        if request.method=="POST":
            username=request.POST['uname']
            pass1=request.POST['password']
            user=authenticate(username=username, password=pass1)
            if user is not None:
                dj_login(request, user)
                messages.success(request, "Successfully logged in")
                return redirect('Amaris')
            else:
                messages.error(request,"Enter Correct Username and password")
                return redirect('login')
        else:
            return render(request,'404.html')

def logout(request):
    dj_logout(request)
    return redirect('login')