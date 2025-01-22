from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



#Giude Classes and methods

##Biult in forms
class add_user_form(UserCreationForm):
    class Meta:
        model= User
        fields=['username','password1','password2','first_name','last_name','email','groups']

class user_form(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email']