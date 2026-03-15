from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Product

# Create your views here.

def login_view(request: HttpRequest):
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if not user:
            messages.error(request, "username yoki parol xato")
            return redirect("login")
        
        login(request,user)
        return redirect("login")
    return render(request, "login.html")

def register_view(request: HttpRequest):

    if request.method == "POST":
        first_name = request.POST.get("first_name", "Anonim")
        last_name = request.POST.get("last_name", "Anonim")
        username = request.POST.get("username")

        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if User.objects.filter(username=username).exists():
            messages.warning(request, "Bunday user mavjud")
            return redirect("register")
       
        if not password1 == password2:
            messages.warning(request, "Parollar mos emas")
            return redirect("register")
        
        user = User.objects.create_user(
            username=username,
            password=password1,
            last_name=last_name,
            first_name=first_name
        )
        return redirect("register")
    return render(request, "register.html")


def index_view(request):
    products = Product.objects.all()
    return render(request,'index.html',{'products':products})

def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    return render(request,'product_detail.html',{'product':product})

