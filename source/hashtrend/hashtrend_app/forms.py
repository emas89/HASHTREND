# IMPORTS

from django import forms
from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserLog

# User registration form
class SignUpForm(UserCreationForm):
	"""
	Form class to register a user
	"""
	email = forms.EmailField(max_length=254, help_text='Please enter a valid email')

class Meta:
	model = User
	fields = ('username', 'email', 'password1', 'password2')