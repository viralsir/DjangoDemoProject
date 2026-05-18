from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_exempt
from student.models import student
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request,"student/home.html")

@csrf_exempt
def addstudent(request):
    if request.method == "POST":
        print(request.POST)
    return HttpResponse("<h1>Add Student</h1>")

def viewstudent(request):
    students = serialize ('json',student.objects.all())

    return JsonResponse({"students":students})
def updatestudent(request):
    return HttpResponse("<h1>Update Student</h1>")

def deletestudent(request):
    return HttpResponse("<h1>Delete Student</h1>")