from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Customer,Expences
from .froms import RegistrationForm,UserCreationForm
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
            users=authenticate(email=email,username=name,password1=pass1)
            login(request,users)
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

def expence(request,id):
    context={
        'expences':Expences.objects.filter(c_name=id),
    }
    return render(request,'expence.html',context)

def delete(request,id):
    delete_data=Expences.objects.get(pk=id)
    delete_data.delete()
    return redirect('home')

# Add a contact view

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

def deleteContact(request,id):
    dlt=Customer.objects.get(pk=id)
    dlt.delete()
    return redirect('home')


    

def addExpence(request):
    Customer_name = Customer.objects.all()
    if request.method == 'POST':
        expence_title=request.POST['title']
        amount=request.POST['amount']
        c_name=request.POST['cname']

        new_expence=Expences.objects.create(expence=expence_title,amount=amount,c_name=Customer.objects.get(name=c_name))
        new_expence.save()
        return redirect('home')
    
    return render(request,'addExpence.html',{'names':Customer_name})

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