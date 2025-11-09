from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def login(request):
    context = {

    }
    return render(request, "users/login.html", context)

def registration(request):
    if request.method == "POST":
        form = UserRegisterForm(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("users:login"))
    else:
        form = UserRegisterForm()
    context = {
        'form':form,
    }
    return render(request, "users/registration.html", context)
    

def profile(request):
    context = {

    }
    return render(request, "users/profile.html", context)

@login_required
def logout(request):
    logout(request)

