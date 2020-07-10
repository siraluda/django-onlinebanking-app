from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import User, CustomerProfile
from django import forms

class UserSignUp(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

class CustomerProfileForm(forms.ModelForm):

    class Meta:
        model = CustomerProfile
        fields = ['phone_number', 'date_of_birth', 'address','city', 'postalcode',]

