from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method=='POST':
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        username = request.POST['user_name']
        email = request.POST['email']
        pswd = request.POST['psw']
        pswrepeat = request.POST['psw-repeat']
        if pswd==pswrepeat:
            if User.objects.filter(username=username).exists():
                messages.info(request,"This Username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"This Email-id already exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=pswd)
                user.save();
                return redirect('login')
                print("user created")
        else:
            messages.info(request,"Password not matching")
            return redirect('register')
        return redirect('/')

    return render(request,'register.html')


def login(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['psw']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Username or Password")
            return redirect('login')
    return render(request,'Login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')