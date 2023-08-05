from django.shortcuts import render
from .models import *
import requests

def homepage(request):
    if request.POST:
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        email=request.POST["email"]
        company=request.POST["company"]
        phone=request.POST["phone"]
        job=request.POST["job"]
        pswd=request.POST["pswd"]
        reg_obj=register.objects.create(fname=fname,lname=lname,email=email,company=company,phone=phone,job=job,pswd=pswd)
        reg_obj.save()
        login_obj=Logindata.objects.create(email=email,pswd=pswd)
        login_obj.save()
    return render(request,"homepage.html")

def login(request):
    
    if request.POST:
        email=request.POST["email"]
        pswd=request.POST["pswd"]
        data=login.objects.filter(email=email,pswd=pswd)
        request.session["email"]=email
       
    return render(request,"login.html")