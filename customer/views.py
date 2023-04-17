from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from .models import Customer,Expences,OneTimePassword
from .froms import RegistrationForm
import random
from .helper import MessageHandler
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.

def logout_customer(request):
    logout(request)
    return redirect('home')
def Register(request):
    form=RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            name=form.cleaned_data['username']
            mobile=form.cleaned_data['phone']
            email=form.cleaned_data['email']
            pass1=form.cleaned_data['password1']
            
            new_customer=Customer.objects.create(name=name,mobile=mobile,email=email,password=pass1)
            new_customer.save()
            user=authenticate(email=email,username=name,password1=pass1)
            login(request,user)
            return redirect('home')
        else:
            return render(request,'index.html',{'form':form})
    return render(request,'index.html',{'form':form})
        

def login_customer(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["pass1"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
          
            return redirect('home')
        else:
            messages.success(request,"incorrect username or password")
            return redirect('login')
    else:
    # forms=RegistrationForm()
        return render(request,'login.html')
def home(request):
    context={
        'customers':Customer.objects.all()
    }
    return render(request,'home.html',context)


@login_required(login_url='login')
def expence(request,id):
    context={
        'expences':Expences.objects.filter(c_name=id),
    }
    return render(request,'expence.html',context)


@login_required(login_url='login')
def delete(request,id):
    delete_data=Expences.objects.get(pk=id)
    delete_data.delete()
    return HttpResponseRedirect(request.path_info)
# Add a contact view


@login_required(login_url='login')
def addContact(request):
    if request.method == 'POST':
        name=request.POST['name']
        mobile=request.POST['mobile']
        email=request.POST['email']
        pass1=request.POST['pass1']
        
        new_employe=Customer.objects.create(name=name,mobile=mobile,email=email,password=pass1)
        new_employe.save()
        return redirect('home')
            
        
    
    return render(request,'addContact.html')

# Update Contact 

@login_required(login_url='login')
def editContact(request,id):
    if request.method == 'POST':
        new_name=request.POST['name']
        new_mobile=request.POST['mobile']
        new_email=request.POST['email']
        new_pass1=request.POST['pass1']
        
        Customer.objects.filter(pk=id).update(name=new_name,mobile=new_mobile,email=new_email,password=new_pass1)
        return redirect('home')
    else:
        context={
        'edit':Customer.objects.get(pk=id)
            
        }
        return render(request,'editContact.html',context)
    

# Delete contact 

@login_required(login_url='login')
def deleteContact(request,id):
    dlt=Customer.objects.get(pk=id)
    dlt.delete()
    return redirect('home')


    

@login_required(login_url='login')
def addExpence(request):
    Customer_name = Customer.objects.all()
    if request.method == 'POST':
        expence_title=request.POST['title']
        amount=request.POST['amount']
        c_name=request.POST['cname']

        new_expence=Expences.objects.create(expence=expence_title,amount=amount,c_name=Customer.objects.get(name=c_name))
        new_expence.save()
        # return redirect('home')
        messages.success(request,'expence added successfully')
        return HttpResponseRedirect(request.path_info)
    
    return render(request,'addExpence.html',{'names':Customer_name})


@login_required(login_url='login')
def editExpence(request,id):
    edit=Expences.objects.get(pk=id)
    if request.method == 'POST':
        
        
        new_title=request.POST['title']
        new_amount=request.POST['amount']
        
        new_expence=Expences.objects.filter(pk=id).update(expence=new_title,amount=new_amount)
        return redirect('home')
    context={
        'edit':Expences.objects.get(pk=id)
    }
    return render(request,'editExpence.html',context)


def loginWithPhone(request):
    if request.method == 'POST':
        if Customer.objects.filter(mobile=request.POST['phone_number']).exists():
            otp=random.randint(1000,9999)
            customer=OneTimePassword.objects.create(mobile=request.POST['phone_number'],otp=f'{otp}')
            if request.POST['methodOtp']:
                messagehandler=MessageHandler(request.POST['phone_number'],otp).send_otp_via_message()
            red=redirect(f'otp/{customer.uid}/')
            red.set_cookie("can_otp_enter",True,max_age=600)
            return red  
        else:
            messages.success(request,'This number not registered..')
    return render(request,'login-with-phone.html')        
        

        
def otpVerify(request,uid):
    if request.method=="POST":
        profile=OneTimePassword.objects.get(uid=uid)    
        if request.COOKIES.get('can_otp_enter')!=None:
            if(profile.otp==request.POST['otp']):
                messages.warning(request,"Otp Verified Successfully")
                red=redirect("home")
                red.set_cookie('verified',True)
                return red
            else:
                messages.info(request,'Wrong otp enter')
                return HttpResponseRedirect(request.path_info)
        return HttpResponse("10 minutes passed")        
    return render(request,"otp.html",{'id':uid})
