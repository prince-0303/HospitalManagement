from django import forms
from .models import Bookings


class DateInput (forms.DateInput) :    # Date Picker
    input_type = 'date'

class BookingForms (forms.ModelForm):
    class Meta :
        model= Bookings
        fields = '__all__'

        widgets = {
            'booking_date' : DateInput   #which model is used to be as a picker
        }

        labels = {
            'patient_name' : 'Patient Name :',
            'patient_phone' : 'Patient Phone :',
            'patient_email' : 'Email :',
            'doc_name': 'Doctor Name :',
            'booking_date' : 'Booking Date :',
        }