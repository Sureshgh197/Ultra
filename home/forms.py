from django import forms
from . models import *
  
class ImageUploadForm(forms.ModelForm):
  
    class Meta:
        model = UImages
        fields = ['imag']

# class DateInput(forms.DateInput):
#     input_type = 'date'

# class UserSignUpForm(forms.ModelForm):
#     class Meta:
#         model = AppUsers
#         fields = ['profile_picture','phone','email','DOB','last_name','first_name','username']
#         widgets = {
#             'DOB': DateInput(),
#         }

class LoginForm(forms.Form):
    email     =forms.CharField(max_length=100)
    password  =forms.CharField(widget=forms.PasswordInput)