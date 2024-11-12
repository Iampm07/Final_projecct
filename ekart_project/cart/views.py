from django.shortcuts import render

from store.models import Product

def home(request):

    products =Product.objects.all() #Query set

    context={
        'products':products
    }
    return render(request,'home.html',context)


def checkout(request):
    return render(request,'store/checkout.html')
