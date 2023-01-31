from django.db import models
from userapp.models import profile

# Create your models here.
class category(models.Model):
  categoryID=models.BigAutoField(verbose_name="ID",primary_key=True)
  categoryname=models.CharField(verbose_name='Categoria',max_length=20)

class imagegallery(models.Model):
  imageID=models.BigAutoField(verbose_name='ID #',primary_key=True)
  imagename=models.CharField(verbose_name='Titulo de Foto',max_length=20)
  image=models.ImageField(verbose_name='Fotografia',upload_to='photos')
  categoryimage=models.ForeignKey('category',on_delete=models.CASCADE)
  imagedescription=models.TextField(verbose_name='descripcion')
  usuario=models.ForeignKey(profile,on_delete=models.CASCADE)