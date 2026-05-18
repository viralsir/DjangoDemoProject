from django.urls import path

from student.views import addstudent, viewstudent, updatestudent,deletestudent

urlpatterns = [
    path("add",addstudent),
    path("view",viewstudent),
    path("update/",updatestudent),
    path("delete/",deletestudent),

]