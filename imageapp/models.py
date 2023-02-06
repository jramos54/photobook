from django.db import models
from userapp.models import profile

from django.template.defaultfilters import slugify
from django.urls import reverse

from django_resized import ResizedImageField

# Create your models here.
class category(models.Model):
  categoryID=models.BigAutoField(verbose_name="ID",primary_key=True)
  categoryname=models.CharField(verbose_name='Categoria',max_length=20)

  slug=models.SlugField(max_length=500,unique=True,blank=True,null=True)

  def __str__(self):
    return self.categoryname
  
  def geturl(self):
    return reverse('categorydetail',kwargs={'slug':self.slug})
  
  def save(self,*args,**kwargs):
    catname=self.categoryname
    self.slug=slugify('{}{}'.format(catname))
    super(category,self).save(*args,**kwargs)

class imagegallery(models.Model):
  imageID=models.BigAutoField(verbose_name='ID #',primary_key=True)
  imagename=models.CharField(verbose_name='Titulo de Foto',max_length=20)
  image=models.ImageField(verbose_name='Fotografia',upload_to='photos')
  categoryimage=models.ForeignKey('category',on_delete=models.CASCADE,verbose_name='categoria')
  imagedescription=models.TextField(verbose_name='descripcion')
  usuario=models.ForeignKey(profile,on_delete=models.CASCADE)

  #squareImage=ResizedImageField(size=[1000,1000],crop=['middle','center'],upload_to='square')
  #landImage=ResizedImageField(size=[2878,1618],crop=['middle','center'],upload_to='landscape')
  #tallImage=ResizedImageField(size=[1618,2878],crop=['middle','center'],upload_to='tall')

  slug=models.SlugField(max_length=500,unique=True,blank=True,null=True)

  def __str__(self):
    return '{}{}'.format(self.imageID,self.imagename)

  def geturl(self):
    return reverse('imagedetail',kwargs={'slug':self.slug})

  def save(self,*args,**kwargs):
    self.slug=slugify('{}{}'.format(self.imageID,self.imagename))
    super(imagegallery,self).save(*args,**kwargs)
    