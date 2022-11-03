from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib import auth
from .models import *

# Create your views here.
def signup(request):

    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')

        if User.objects.filter(username=username):
                return redirect('signup')

        if User.objects.filter(email=email).exists():
            return redirect('signup')

        if password != confirmpassword:
            return redirect('signup')

        user=User.objects.create_user(username,email,password)

        user.save()

        return redirect('login')

    return render(request,'authentication/signup.html')

def signup_redirect(request):
    messages.error(request, "Something wrong here, it may be that you already have account!")
    return redirect("home")

def login(request):
    if request.method=='GET':
        return render(request,'authentication/login.html')
    else:
        user = auth.authenticate(username=request.POST.get('username'),password = request.POST.get('password'))

        if user is not None:
            auth.login(request,user)
            names=dept.objects.all()
            return render(request,'authentication/dashboard.html',{'names': names})
        else:
            return render (request,'authentication/login.html')

def logout(request):
    auth.logout(request)
    return render(request,'authentication/login.html')

def home(request):
    names=dept.objects.all()
    return render(request,'authentication/dashboard.html',{'names': names})

def events(request,id):
    names=dept.objects.all()
    infos=dept_events.objects.filter(dashboard_id=id)
    context={'infos':infos,'names':names}
    return render(request,'authentication/main.html',context)

def club(request):
    ev_cl=club_events.objects.all()
    names=dept.objects.all()
    details=clubs.objects.all()
    context2={'details':details,'names':names,'ev_cl':ev_cl}
    return render(request,'authentication/club.html',context2)

def clubev(request,id):
    names=dept.objects.all()
    ev_cl=club_events.objects.filter(clubs_id=id)
    context={'ev_cl':ev_cl,'names':names}
    return render(request,'authentication/clubev.html',context)

def ach(request,id):
    names=dept.objects.all()
    ach_obj=achievers.objects.filter(dept_id=id)
    context={'names':names,'ach_obj':ach_obj}
    return render(request,'authentication/achiever.html',context)





