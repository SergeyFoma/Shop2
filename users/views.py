from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm, UserLoginForm, UserProfileForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
#from django.contrib.auth import authenticate


def login_user(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect(reverse('users:profile'))
    else:
        form = UserLoginForm()
    context = {
        "form":form,

    }
    return render(request, "users/login_user.html", context)

def registration(request):
    if request.method == "POST":
        form = UserRegisterForm(data = request.POST)
        if form.is_valid():
            form.save()
            user=form.instance
            login(request, user)
            return HttpResponseRedirect(reverse("users:profile"))
    else:
        form = UserRegisterForm()
    context = {
        'form':form,
    }
    return render(request, "users/registration.html", context)
    

@login_required
def profile(request):
    if request.method == "POST":
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileForm()
    context = {
        'form':form,
    }
    return render(request, "users/profile.html", context)

@login_required
def logout_user(request):
    logout(request)
    return redirect(reverse("main:index"))

