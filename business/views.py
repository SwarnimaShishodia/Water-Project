from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from user.models import Plan,Subscribe,Feedback
from django.conf import settings
from . import forms,models
from .forms import Company
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
    

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

def addplan(request):
    if(request.method=='POST'):
        #user=User.objects.get(username=request.user.username)
        name=request.user.username
        #print(name)
        price=request.POST.get('price')
        title=request.POST.get('duration')
        desc=request.POST.get('desc')
        plan=Plan(planowner=name,price=price,title=title,dsc=desc)
        plan.save()
        messages.success(request,'Plan added successfully')
        return redirect('plan')
    return render(request,'addplan.html')
def companyregister(request):
    companyForm=forms.Company()
    if request.method=='POST':
        companyForm=forms.Company(request.POST, request.FILES)
        print("Yes")
        if companyForm.is_valid():
            companyForm.save()
        return HttpResponseRedirect('companyregister')
    return render(request,'companyregister.html',{'companyForm':companyForm})
    
@staff_member_required
def adminclick_view(request):
    if request.user.is_superuser:
        return HttpResponseRedirect('admindashboard')
    return HttpResponseRedirect('plan')

#@login_required(login_url='adminlogin')
@staff_member_required
def admin_dashboard_view(request):
    customercount=User.objects.all().count()
    plancount=Plan.objects.all().count()
    ordercount=Subscribe.objects.all().count()
    suppliercount=models.Supplier.objects.all().count()

    suppliers=models.Supplier.objects.all()
    mydict={
    'customercount':customercount,
    'plancount':plancount,
    'ordercount':ordercount,
    'suppliercount':suppliercount,
    'suppliers':suppliers,
    }
    return render(request,'admin_dashboard.html',context=mydict)

#@login_required(login_url='adminlogin')
@staff_member_required
def delete_supplier_view(request,pk):
    supplier=models.Supplier.objects.get(email=pk)
    supplier.delete()
    return redirect('admindashboard')

#@login_required(login_url='adminlogin')
@staff_member_required
def admin_complains(request):
    

    complains=Feedback.objects.all()
    mydict={
    
    'complains':complains,
    }
    return render(request,'admincomplain.html',context=mydict)
#@login_required(login_url='adminlogin')
@staff_member_required
def delete_complain_view(request,pk):
    complain=Feedback.objects.get(id=pk)
    complain.delete()
    return redirect('complains')