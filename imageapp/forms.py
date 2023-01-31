from django import forms
from .models import category,imagegallery

class newcategoryform(forms.ModelForm):
  class Meta:
    model=category
    fields=('categoryname',)

class uploadimageform(forms.ModelForm):
  class Meta:
    model=imagegallery
    fields=('imagename','image','categoryimage','imagedescription')