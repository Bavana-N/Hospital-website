from django.db import models
from django.contrib.auth.models import User
class Department(models.Model):
    image=models.ImageField(upload_to="Dept/")
    name=models.CharField(max_length=255)
    desc=models.TextField()
    about=models.TextField()
    service1=models.CharField(max_length=255)
    service2=models.CharField(max_length=255)
    service3=models.CharField(max_length=255)
    service4=models.CharField(max_length=255)
    def __str__(self):
        return self.name
# Doctor Table
class Doctor(models.Model):
    image = models.ImageField(upload_to='Doctors/')
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    experience = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
#Booking table
class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    time_slot = models.CharField(max_length=20)
    visit_type = models.CharField(max_length=50)
    patient_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_name



