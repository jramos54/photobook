from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import newcategoryform,uploadimageform

from .models import category, imagegallery

# Create your views here.
def addimage(request):
  template=loader.get_template('imageapp/imageupload.html')

  if request.method == 'POST':
    imageform=uploadimageform(request.POST)
    if imageform.is_valid():
      imageform.save()
      return HttpResponseRedirect(reverse('/'))
  else:
    imageform=uploadimageform

  context={'form':imageform}
  return HttpResponse(template.render(context,request))

def newcategory(request):
  template=loader.get_template('imageapp/imagecategory.html')
  categoryform=newcategoryform
  if request.method == 'POST':
    categoryform=newcategoryform(request.POST)
    if categoryform.is_valid():
      categoryform.save()
      return redirect('/')
  
  context={'form':categoryform}
  return HttpResponse(template.render(context,request))