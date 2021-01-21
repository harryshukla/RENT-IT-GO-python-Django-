from django.urls import path
from cat import views

urlpatterns = [
    
    path('electronics',views.ecat,name ='cat1'),
    path('cloths',views.ccat,name ='cat2'),
    path('furniture',views.fcat,name ='cat3'),
    path('vehicals',views.vcat,name ='cat4'),
    path('camera',views.pcat,name ='cat5'),
   ]