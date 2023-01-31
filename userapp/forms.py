from django import forms
from .models import profile
from django.db.auth.contrib.models import User

class UserForm(forms.Model):
  model = User
  fields = ('first_name', 'last_name', 'email')

class profileForm(forms.Models):
  model=profile
  fields='__all__'