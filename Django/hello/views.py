from django.http import HttpResponse #import the ability to take http response
from django.shortcuts import render

# Create your views here.
# The function take the http request and send http response containt hello message
def index(request):
    return HttpResponse("Hello!")
def Abdelkhalek(request):
    return HttpResponse("Hello, Abdelkhalek!")
def Boutahri(request):
    return HttpResponse("Hello, Boutahri!")
# def greet(request, name):
#     return HttpResponse(f"Hello, {name.capitalize()}!")
def templates(request):
    return render(request, "hello/index.html")
def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize
    })