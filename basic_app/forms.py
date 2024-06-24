
from django import forms
from django.core import validators
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

#form for UserProfile Info model
class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model=User
        fields=('username','email','password')
    #model user will contain the above fields
    
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('portfolio_site','profile_pic') #we didn't include the 'user' field here