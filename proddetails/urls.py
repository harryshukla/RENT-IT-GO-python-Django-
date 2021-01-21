from django.urls import path
from proddetails import views

urlpatterns = [
   
   
    path("productdetail/<int:myid>",views.productdetail,name ='productdetail'),
    path("productdetail/productdetail/<int:myid>",views.productdetail,name ='productdetail'),       
]