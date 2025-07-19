from django.shortcuts import render
from django.http import HttpResponse

from .models import Departments, Doctors
from .forms import BookingForms

# Create your views here.

def index(request) :
    return render(request, "index.html")

def about(request) :
    return render(request, "about.html")

def booking(request) :
    if request.method =='POST':
        form = BookingForms(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    form = BookingForms()
    dict_forms ={
        'form' : form
    }
    return render(request, "booking.html", dict_forms)

def doctor(request) :
    dict_docs ={
        'doctors' : Doctors.objects.all()
    }
    return render(request, "doctor.html", dict_docs)

def contact(request) :
    return render(request, "contact.html")

def department(request) :
    dict_dept ={
        'dept' : Departments.objects.all()
    }
    return render(request, "department.html", dict_dept)