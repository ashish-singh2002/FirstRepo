from django.shortcuts import render
from Mainapp.models import *

def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def Registration(request):
    return render(request,"Registration.html")
def login(request):
    return render(request,"login.html")
def contact(request):
    return render(request,"contact.html")



