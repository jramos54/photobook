from django.db import models

# Create your models here.

class visitors(models.Model):
  visitorID=models.BigAutoField(verbose_name='Visitante #',primary_key=True)
  name=models.CharField(verbose_name='Nombre',max_length=20)
  email=models.EmailField(verbose_name='Correo Electronico',max_length=50)
  coments=models.TextField(verbose_name='Comentarios',max_length=200)
