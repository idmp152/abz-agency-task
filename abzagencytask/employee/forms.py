from django import forms
# from .models import Employee

class BetaRegistrationForm(forms.Form):
    login = forms.CharField(max_length=255)
    password = forms.CharField(max_length=32)
