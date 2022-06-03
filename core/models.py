from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Users(AbstractUser):
    # username = models.CharField(null=False, max_length=20, unique=True)
    email = models.EmailField(verbose_name='email', max_length=50, unique=True)
    phone = models.CharField(null=True, max_length=50)
    REQUIRED_FIELDS = ['username', 'phone', 'first_name', 'last_name']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email


class Doctor(models.Model):
    Gender = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    ]
    NMC_no = models.CharField(max_length=10, unique=True)
    First_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    Gender = models.CharField(max_length=8, choices=Gender, default='male')
    Contact_no = models.CharField(max_length=20, unique=True)
    Email = models.CharField(max_length=40, null=True, blank=True)
    Address = models.CharField(max_length=40)
    Hospital_worked_at = models.CharField(max_length=30)
    Specialist = models.CharField(max_length=30)
    About_me = models.CharField(max_length=500)

    def __str__(self):
        return self.First_name


class Patient(models.Model):
    Gender = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    ]

    Blood_group = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-')
    ]

    First_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    Gender = models.CharField(max_length=8, choices=Gender, default='male')
    Blood_group = models.CharField(max_length=5, choices=Blood_group, default='A+')
    Contact_no = models.CharField(max_length=20)
    Email = models.CharField(max_length=40)
    Address = models.CharField(max_length=40)

    def __str__(self):
        return self.First_name


class Blog(models.Model):
    Topic = models.CharField(max_length=100)
    Written_Date = models.DateField()
    Written_By = models.CharField(max_length=40)
    Content = models.CharField(max_length=1200)

    def __str__(self):
        return self.Topic


class Appointment(models.Model):
    Appointment_type = [
        ('Online', 'Online'),
        ('Hospital Visit', 'Hospital Visit')
    ]
    Appointment_date = models.DateField()
    Appointed_doctor = models.CharField(max_length=40)
    Appointment_type = models.CharField(max_length=20, choices=Appointment_type, default='Online')
    Patient_Name = models.CharField(max_length=40)
    Time = models.TimeField(null=False)
    Price = models.IntegerField(blank=True)

    def __str__(self):
        return self.Appointed_doctor


class Query(models.Model):
    Question = models.CharField(max_length=500)
    Ask_to_specialist = models.CharField(max_length=50)

    def __str__(self):
        return self.Ask_to_specialist

class Medical_report(models.Model):
    Medical_report = models.ImageField(null=False)
    Name = models.CharField(max_length=50)
    Tested_at = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

