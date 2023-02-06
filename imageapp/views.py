from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import newcategoryform,uploadimageform

from .models import category, imagegallery

# Create your views here.
def addimage(request):
  template=loader.get_template('imageapp/imageupload.html')
  imageform=uploadimageform
  if request.method == 'POST':
    imageform=uploadimageform(request.POST,request.FILES)
    if imageform.is_valid():
      imageform.save()
      return redirect('/')

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

def categorydetail(request,slug):
  template=loader.get_template('imageapp/categorydetail.html')
  categoryslug=category.objects.get(slug=slug)
  images=imagegallery.objects.filter(category=categoryslug).order_by('-imagename')
  context={'images':images,'category':categoryslug}

  return HttpResponse(template.render(context,request))

  
def imagedetail(request,slug):
  template=loader.get_template('landingapp/index.html')
  categorys=category.objects.get(slug=slug1)
  images=imagegallery.objects.get(slug=slug2)
  context={'category':categorys,'image':images}
  return HttpResponse(template.render(context,request))
