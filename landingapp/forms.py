from django import forms
from .models import visitors

class commentform(forms.ModelForm):
  class Meta:
    model=visitors
    fields='__all__'