from django import forms
from .models import profile
from django.db.auth.contrib.models import User

class UserForm(forms.Model):
  model = User
  fields = '__all__'

class profileForm(forms.Models):
  model=profile
  fields='__all__'