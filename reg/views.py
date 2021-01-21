from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth,User
from django.contrib import messages

# Create your views here.

def reg(request):
    if(request.method=="POST"):#checking method of rgister and browser rquest
        full_name=request.POST['full_name']
        email=request.POST['email']
        user_name=request.POST['user_name']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if(password==confirm_password):
            if User.objects.filter(username=user_name).exists():
                messages.info(request,"username taken")
                return redirect("reg")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect("reg")
            else:
                user=User.objects.create_user(username=user_name,email=email,password=password)# creating user in data base
                user.save() #saving in dtatbase
                print("user created sucessfully")
                return redirect("login")
                
              
                
        else:
            messages.info(request,"not matching")
            return redirect('registration') 
        return redirect('/')   
    else:
         return render(request,'registration.html')