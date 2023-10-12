from urllib.parse import parse_qs
from django.contrib.auth.base_user import password_validation
from django.shortcuts import redirect, render
from django.urls.resolvers import re
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        username = fname
        email = request.POST.get("email")
        number = request.POST.get("number")
        # date = request.POST.get("date")
        # date = date.strftime("%m/%d/%Y")
        gender  = request.POST.get("gender")
        address  = request.POST.get("address")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")
 
        my_user = User.objects.create_user(username, email, password)
        my_user.first_name = fname
        my_user.last_name = lname
        my_user.save()
        messages.success(request, "Account has been created.")
        return redirect('signin')
    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(email = email, password = password)
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "index.html", {'fname': fname})

        else:
            messages.error(request,"Wrong credentials!!")
            return redirect('signin')
    return render(request, 'signin.html')

def signout(request):
    return render(request, 'signout.html')
