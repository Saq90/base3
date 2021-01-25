from django.shortcuts import render,redirect
from . models import Product , Contact
from math import ceil

def home(request):
    products= Product.objects.all()
    n= len(products)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    return render(request,"home.html", params)


def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        address=request.POST.get('address', '')
        contact = Contact(name=name, email=email, phone=phone,address=address)
        contact.save()
        return redirect('/')
    return render(request,'contact.html')