from django.db import models
import uuid
# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=12,unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name + self.mobile

class OneTimePassword(models.Model):
    mobile=models.CharField(max_length=12,unique=False)
    otp=models.CharField(max_length=100,null=True,blank=True)
    uid=models.CharField(default=f'{uuid.uuid4}',max_length=200)
    
    def __str__(self) -> str:
        return self.mobile + ' :  ' +self.otp


class Expences(models.Model):
    expence=models.CharField(max_length=100)
    amount=models.DecimalField(max_digits=7,decimal_places=2)
    Entry_date=models.DateField(auto_now=True)

    c_name=models.ForeignKey(Customer,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.c_name)