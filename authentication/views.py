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
        email = request.POST.get("email")
        username = email
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")


        if not password == cpassword:
            messages.error(request, "password and confirm password doesnt match.")
            return redirect('signup')

        existing_user = User.objects.filter(username=username)
        if existing_user.exists():
            messages.error(request, "User with that username already exixts")
            return redirect('signup')


        my_user = User.objects.create_user(username=username, email=username, password=password,first_name=fname,last_name=lname)
        if my_user:
            my_user.save()
            messages.success(request, "Account has been created.")
            return redirect('signin')

        
    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(username = email, password = password)
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
