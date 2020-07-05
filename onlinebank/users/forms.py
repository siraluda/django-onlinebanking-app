from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import models
from .models import User

class UserSignUp(UserCreationForm):

    class Meta(UserCreationForm):
        model=User
        fields = ('first_name','last_name','email','password1', 'password2')





