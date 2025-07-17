from django.db import models

# Create your models here.

class Departments (models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()

class Doctors (models.Model):
    doc_name = models.CharField(max_length=100)
    doc_speciality = models.CharField(max_length=150)
    dep_name = models.ForeignKey(Departments, on_delete= models.CASCADE)
    doc_img = models.ImageField(upload_to='doctors')