from django.shortcuts import render,redirect
from . models import Product,Contact
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate, login, logout
from math import ceil
def home(request):
    products= Product.objects.all()
    n= len(products)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    return render(request,"home.html", params)


def about(request):
    return render(request,'about.html')



def register(request):
    if request.method == 'POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        user=User.objects.create_user(first_name=first_name,last_name=last_name, username=username,email=email,password=password)
        user.save()
        return redirect('/')


    return render (request,'register.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        address=request.POST.get('address', '')
        contact = Contact(name=name,phone=phone,address=address)
        contact.save()
        return redirect('/')
    return render(request,'contact.html')


def Login(request):
    if request.method=="POST":

        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        user.save()
        if user is not None:
            login(request, user)

            return redirect('/')
    return render(request,'Login.html')


def Logout(request):
    logout(request)
    return redirect('home')






















