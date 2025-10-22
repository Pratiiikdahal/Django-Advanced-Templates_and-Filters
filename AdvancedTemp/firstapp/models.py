from django.db import models

# Create your models here.

class Employee(models.Model):
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    phone=models.IntegerField(null=True,blank=True,max_length=15)
    hire_date=models.DateField()
    job_title=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)