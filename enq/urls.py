from django.urls import path
from . import views

urlpatterns = [
    path('contact',views.enq,name ='enq'),
    
    path('productdetail/contact',views.enq,name ='enq'),

   
    
    
]