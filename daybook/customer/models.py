from django.db import models

# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100,unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
# insert=Customer.objects.create(name="namshad",mobile='9946739488',email='namshad@gmail.com',password='1234')
# insert.save()

class Expences(models.Model):
    expence=models.CharField(max_length=100)
    amount=models.DecimalField(max_digits=7,decimal_places=2)
    Entry_date=models.DateField(auto_now=True)

    c_name=models.ForeignKey(Customer,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.c_name)