from django.shortcuts import render
from django.http import HttpResponse

from .models import Departments
# Create your views here.

def index(request) :
    return render(request, "index.html")

def about(request) :
    return render(request, "about.html")

def booking(request) :
    return render(request, "booking.html")

def doctor(request) :
    return render(request, "doctor.html")

def contact(request) :
    return render(request, "contact.html")

def department(request) :
    dict_dept ={
        'dept' : Departments.objects.all()
    }
    return render(request, "department.html", dict_dept)