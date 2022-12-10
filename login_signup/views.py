from django.shortcuts import render, redirect
from django.http import HttpResponse
from  django.contrib.auth.models import User ,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def login(request):
    if request.user.is_authenticated :
        return redirect('crud/view')
    else:
        if request.method == "POST":
            username=request.POST["username"]
            password =request.POST["password"]
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                # messages.success(request,"login sucessfull")
                return redirect('crud/view')
            else:
                messages.info(request,"The username or password that you've entered doesn't match any account")
                return redirect("login")

        return render(request,"login.html")


def register(request):
    if request.user.is_authenticated :
        return redirect('crud/view')
    else:
        if request.method == "POST":
            username=request.POST["username"]
            email=request.POST["email"]
            password=request.POST["password"]
            password2=request.POST["password2"]
            first_name=request.POST['firstname']
            last_name=request.POST['lastname']

            if password == password2:
                if User.objects.filter(email=email).exists():
                    messages.info(request,"Email already used")
                    return redirect("register")
                elif User.objects.filter(username=username).exists():
                    messages.info(request,"username already exist")
                    return redirect("register")
                elif User.objects.filter(first_name=first_name).exists():
                    messages.info(request,"first_name already exist")
                    return redirect("register")
                else:
                    user =User.objects.create_user(username=username,email=email,password=password ,first_name=first_name,last_name=last_name)
                    user.save()
                    return redirect("login")
            else:
                messages.info(request,"password doesn't match")
                return redirect("register")
        else:
            return render(request,"register.html")        



def logout(request):
    auth.logout(request)
    return redirect("login")