from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Medicine
from django.contrib.auth.decorators import login_required



def register_view(request):
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        User.objects.create_user(username=name, password=password)

        return redirect('login')

    return render(request, 'register.html')





def login_view(request):
    if request.method == "POST":
        username = request.POST ['username']
        password = request.POST ['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')



def logout_view(request):
    logout(request)
    return redirect('login')



@login_required
def home(request):
    return render(request, 'home.html')



