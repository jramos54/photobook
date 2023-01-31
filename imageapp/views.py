from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import newcategoryform,uploadimageform

from .models import category, imagegallery

# Create your views here.
def addimage(request):
  pass

def newcategory(request):
  template=loader.get_template('imageapp/imagecategory.html')
  
  if request.method == 'POST':
    categoryform=newcategoryform(request.POST)
    if categoryform.is_valid():
      return HttpResponseRedirect(reverse('/'))
  else:
    categoryform=newcategoryform()
  
  context={'form':categoryform}
  return HttpResponse(template.render(),context)