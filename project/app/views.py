
from .models import Student
from django.shortcuts import render
from django.http import HttpResponse
def home(request):
#    return  HttpResponse ("hello")
    data =Student.objects.create(
          stu_name = 'arpit',
          stu_email = 'arpit@gmail.com',
          stu_city = 'indore'  
    )
    # data =Student.objects.get(id=1)       #return single object

    # print(data.id )
    # print(data.stu_name)
    # print(data.stu_email )
    # print(data.city)
    
