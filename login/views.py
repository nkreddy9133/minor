from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import pics,Profile

import random
username=""
def home(request):
    return render(request,'home.html',{'username':username})

def login(request):
    if request.method == 'POST' :
        print(request.POST)
        username = request.POST['username']
        password =  request.POST['pass']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            if Profile.objects.filter(username=username).exists():
                if Profile.objects.filter(email=user.email).exists():
                    return redirect("home")
            else :
                p=Profile(username=username,email=user.email,fullname=user.first_name)
                print(p)
                p.save();
            return redirect("home")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else :
        pic=list(pics.objects.all())
        p=[]
        for i in range(len(pic)):
            x=random.choice(pic)
            pic.remove(x)
            p.append(x)
        return render(request,'login.html',{'pics':p})

def register(request):
    if request.method == 'POST' :
        print(request.POST)
        FullName = request.POST['fullname']
        UserName = request.POST['username']
        Password =  request.POST['pass']
        Email = request.POST['email']
        if User.objects.filter(username=UserName).exists():
            messages.info(request,"That username is taken.Try another.")
            return redirect('register')
        elif User.objects.filter(email=Email).exists():
            messages.info(request,"That email is taken.Try another.")
            return redirect('register')
        elif UserName=="" or Password=="" or FullName=="" or Email=="":
            messages.info(request,"Enter Complete details.")
            return redirect('register')

        else :
                messages.info(request,"Account created successfully.")   
                user = User.objects.create_user(first_name=FullName,username=UserName,email=Email,password=Password)
                p=Profile(fullname=FullName,username=UserName,email=Email,password=Password)
                print(p)
                p.save()
                user.save()
                return redirect('login')
    else :   
        pic=list(pics.objects.all())
        p=[]
        for i in range(len(pic)):
            x=random.choice(pic)
            pic.remove(x)
            p.append(x)
        return render(request,'register.html',{'pics':p})

def logout(request):
    auth.logout(request)
    return redirect('login')