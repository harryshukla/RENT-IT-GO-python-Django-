from django.urls import path
from reg import views

urlpatterns = [
    path('registration',views.reg,name ='reg'),
   
    
    
]