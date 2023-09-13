from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world!")

def greet_user(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}")

def welcome_user(request, username):
    return render(request,"hello/index.html",{
        "username": username,
    })
