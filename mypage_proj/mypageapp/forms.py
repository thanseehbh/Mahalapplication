from django import forms
from django.core import validators
from mypageapp.models import *
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password',)
class UserProfDet(forms.ModelForm):
    class Meta():
        model = UserProfInfoA
        fields = ('portfolio_site','location','document',)
