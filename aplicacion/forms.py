from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product


class UserForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password1 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','platform','description','price','quantity','image']
