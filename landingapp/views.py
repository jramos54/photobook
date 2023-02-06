from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from imageapp.models import imagegallery,category

# Create your views here.
def index(request):
  template=loader.get_template('landingapp/index.html')
  categorys=category.objects.all().values()
  fotos=imagegallery.objects.all().values()
  context={'categorias':categorys,'fotos':fotos}
  return HttpResponse(template.render(context,request))
