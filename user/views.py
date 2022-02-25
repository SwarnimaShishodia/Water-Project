from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . models import Plan
from . models import Subscribe
from . models import Reviews
from . models import Feedback
from business.models import Supplier
def index(request):
     return render(request,'home.html')


def user_register(request):
    if(request.method=='POST'):
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if(pass1!=pass2):
            messages.warning(request,'Passwords do not match. Try Again!!')
            return redirect('register')
        elif(User.objects.filter(username=uname).exists()):
            messages.warning(request, 'Username not available')
            return redirect('register')
        elif(User.objects.filter(email=email).exists()):
            messages.warning(request, 'The user already exists.')
            return redirect('register')
        else:
            user= User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=pass1)
            user.save()
            messages.success(request,'You are successfully registered!')
            return redirect('login')
    return render(request,'register.html')

def user_login(request):
    if(request.method=='POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('plan')
        else:
            messages.warning(request,'User is not registered')
            return redirect('register')

    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('/')

def user_feedback(request):
    return render(request,'feedback.html')

def user_subscribe(request,id):
    return render(request,'subscribe.html')

def user_payment(request):
    return render(request,'payment.html')

def user_plan(request):
    plan=Plan.objects.all()
    context={'plans':plan}
    return render(request,'plan.html',context)

def feedback(request):
    if(request.method=='POST'):
        name=request.POST.get('name')
        address=request.POST.get('address')
        mobile=request.POST.get('mobile')
        content=request.POST.get('content')
        feedback=Feedback(name=name, address=address, mobile=mobile, content=content) 
        feedback.save()
        
        return redirect('/')
    return render(request,'feedback.html')


def reviews(request):
    r=Reviews.objects.all()
    r=r[::-1]
    if request.method == 'POST':
        content= request.POST.get('content')
        print(content)
        post=Reviews(content=content)
        post.save()
                
        return redirect('reviews')
    return render(request, 'reviews.html', {'rev':r})



def details(request):
    if(request.method=='POST'):
        name=request.POST.get('Name')
        email=request.POST.get('email')
        mobno=request.POST.get('mno')
        address=request.POST.get('add')
        if(Subscribe.objects.filter(pk=email).exists()):
           messages.warning(request,'You have already subscribed a plan')
           return redirect('plan') 
        subs=Subscribe(name=name, email=email, plansubscribed=1,mobno=mobno,address=address)
        subs.save()
        messages.success(request,'Details have been added successfully, now make payment')
        return redirect('payment')
    
