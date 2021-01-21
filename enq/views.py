from django.shortcuts import render
from django.http import HttpResponse
from .models import contact


# Create your views here.

def enq(request):
    if request.method=="POST":
       name = request.POST.get('name', '')
       email = request.POST.get('email', '')
       message = request.POST.get('mess','')
       phone = request.POST.get('phone', '')
       contac = contact(name=name, email=email, message=message, phone=phone,)
       contac.save()
       return render(request,'contact.html')
    return render(request,'contact.html')
