from django.contrib import admin
from .models import Departments, Doctors, Bookings
# Register your models here.

admin.site.register(Departments)
admin.site.register(Doctors)

class BookingAdmin(admin.ModelAdmin):
    list_display =('id','patient_name','patient_phone','patient_email','doc_name','booking_date','booking_time')

admin.site.register(Bookings, BookingAdmin)
