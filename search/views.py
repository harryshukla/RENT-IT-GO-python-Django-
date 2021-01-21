from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product
from cat.models import cloths,camera,furnitures,electronics,vehical

# Create your views here.


def search(request):
    query=request.POST['query']
    data=Product.objects.filter(product_name__icontains=query)
    data1=cloths.objects.filter(product_name__icontains=query)
    data2=furnitures.objects.filter(product_name__icontains=query)
    data3=camera.objects.filter(product_name__icontains=query)
    data4=electronics.objects.filter(product_name__icontains=query)
    data5=vehical.objects.filter(product_name__icontains=query)
    msg="search results"
    return render(request,'search.html',{'catty':data,'catty1':data1,'catty2':data2,'catty3':data3,'catty4':data4,'catty5':data5,'mseg':msg})
   

