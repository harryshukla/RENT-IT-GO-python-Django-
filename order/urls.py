from django.urls import path
from . import views

urlpatterns = [
    path('shop/checkout/',views.checkout,name ='index'),
    path('tracker',views.tracker,name ='tracker'),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
    
    
   
    
    
]