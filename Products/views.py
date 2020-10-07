from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'products/dashboard.html', {'items': products})



def new(request):
    return render(request, 'products/new.html')


def customer(request):
    return render(request, 'products/customer.html')
