from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def sayhello(request):
    return HttpResponse("Hello World!")

def aboutus(request):
    return HttpResponse("<h1>Aboutus</h1>")
def homepage(request):
    return HttpResponse("<h1>Homepage</h1>")
def contactus(request):
    return HttpResponse("<h1>Contacts</h1>")