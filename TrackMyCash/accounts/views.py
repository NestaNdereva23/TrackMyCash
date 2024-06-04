from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpRequest
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


#landingpage view
def landingpage(request):
    return render(request, "accounts/landingpage.html")


#userregistration
def registrationPage(request):
    form = CreateUserForm(request.POST)

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            user = form.cleaned_data.get('username')
            messages.success(request, "Hello, " +user   )
            return redirect('login')


    return render(request, "registration/register.html", {"form":form})
    

#Userlogin view
def loginPage(request):
    
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return ("Invalid login")

    return render(request, "registration/login.html")

#dashboard view
@login_required
def dashboard(request):
    return render(request, "accounts/dashboard.html")

#userlogout view
@login_required
def logoutPage(request):
    logout(request)
    return redirect('landingpage')