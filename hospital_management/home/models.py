from django.db import models

# Create your models here.

class Departments (models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()

    def __str__(self):
        return self.dep_name
    
class Doctors (models.Model):
    doc_name = models.CharField(max_length=100)
    doc_speciality = models.CharField(max_length=150)
    dep_name = models.ForeignKey(Departments, on_delete= models.CASCADE)
    doc_img = models.ImageField(upload_to='doctors')

    def __str__(self):
        return 'Dr ' + self.doc_name + ' - (' + self.doc_speciality + ')'

class Bookings (models.Model):
    patient_name = models.CharField(max_length=100)
    patient_phone = models.CharField(max_length=10)
    patient_email = models.EmailField()
    doc_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_time = models.DateField(auto_now=True)

    def __str__(self):
        return self.patient_name