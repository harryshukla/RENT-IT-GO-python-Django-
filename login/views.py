from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.contrib.auth.models import auth,User
# Create your views here.

def login(request):
    if(request.method == "POST" ):
       
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if(user != None):
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid user pass')
            return redirect('/login')
    else:
        return render(request,'login.html')
        
    


        
def logout(request):
    auth.logout(request)
    return redirect('/')

