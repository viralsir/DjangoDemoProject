from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def addstudent(request):
    return HttpResponse("<h1>Add Student</h1>")

def viewstudent(request):
    return HttpResponse("<h1>View Student</h1>")
def updatestudent(request):
    return HttpResponse("<h1>Update Student</h1>")

def deletestudent(request):
    return HttpResponse("<h1>Delete Student</h1>")