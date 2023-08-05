from django.db import models

# Create your models here.
class register(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    company=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    phone=models.IntegerField(default=0 )
    pswd=models.CharField(max_length=12)
class Logindata(models.Model):
    email=models.EmailField(max_length=100)
    pswd=models.CharField(max_length=12)