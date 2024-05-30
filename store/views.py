from django.shortcuts import render


def main(request):
    context={}
    return render(request,'store/main.html',context)

def products(request):
    context={}
    return render(request,'store/products.html',context)

def cart(request):
    context={}
    return render(request,'store/cart.html',context)

def checkout(request):
    context={}
    return render(request,'store/checkout.html',context)
