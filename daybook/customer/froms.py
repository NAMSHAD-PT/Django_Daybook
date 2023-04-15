from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    username=forms.CharField(label='Name',widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    email=forms.EmailField(label='Emailllll',widget=forms.EmailInput(attrs={'class':'form-control'}))
    phone=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model=User
        fields=('username','email','phone','password1','password2')
     

        
        # widgets = {
        #     'username':forms.TextInput(attrs={'class':'form-control'}),
        #     # 'password1':forms.TextInput(attrs={'class':'form-control'}),
        #     # 'password2':forms.TextInput(attrs={'class':'form-control'}),
        #     'help':forms.Textarea(attrs={'class':'form-control'}),
        # }