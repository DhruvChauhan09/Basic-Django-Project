from django.shortcuts import render
from datetime import datetime
from home.models import Login
from home.models import Contacts
# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        login = Login(username=username , password=password , date=datetime.today())
        login.save()

    return render(request, "login.html")

def index(request):
    return render(request, "index.html")

def settings(request):
    return render(request, "settings.html") 

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contacts = Contacts(name=name , email=email , phone=phone , desc=desc , date=datetime.today())
        contacts.save()
    return render(request,"contacts.html")

def services(request):
    return render(request, "services.html")

def about(request):
    return render(request, "about.html")