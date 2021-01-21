from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product
from math import ceil
# Create your views here.


def productdetail(request, myid):
    pro=Product.objects.filter(id=myid)    
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products,'prod':pro[0]}
    
    return render(request,'product-detail.html',params)
