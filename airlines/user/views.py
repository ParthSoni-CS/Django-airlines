from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    if not request.user.is_authenticated :
        return HttpResponseRedirect(reverse("user-login"))
    else:
        return render(request,'user/usr.html')


def loginview(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password= password) #admin User module , user
        if user is not None:
            login(request,user) #session
            return HttpResponseRedirect(reverse("user-home"))
        else:
            return render(request,'user/login.html',{
              'message': "Username or password is invalid"
            })

    return render(request,'user/login.html')

def logoutviews(request):
    logout(request)
    return HttpResponseRedirect(reverse("user-login"))
# Create your views here.
