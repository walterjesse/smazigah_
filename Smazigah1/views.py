from django.shortcuts import render, redirect
from django.contrib.auth import logout


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def forgot(request):
    return render(request, 'forgot.html')


def services(request):
    return render(request, 'services.html')


def logout_view(request):
    logout(request)
    return redirect('index')
