from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
            
        if user is not None:
                auth.login(request,user)
                return redirect("/")
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html') 

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'The Username has been taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'The email exists in the Database already')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,  password=password1, email=email)
                user.save();
                messages.info(request, 'User created. Please Login to Continue...')
                return redirect('login')
        else:
            print("The Passwords are not matching")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')    


