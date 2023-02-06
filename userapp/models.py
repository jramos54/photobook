from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class profile(models.Model):
  opciones=(('FOTOGRAFO','FT'),('CLIENTE','CL'))
  iduser=models.BigAutoField(verbose_name='ID Usuario',primary_key=True)
  user=models.OneToOneField(User, on_delete=models.CASCADE)
  ubicacion=models.CharField(verbose_name='Ubicacion',max_length=50)
  type=models.CharField(verbose_name='Rol',choices=opciones,default='', max_length=10)

  def __str__(self):
     return self.user.first_name
  
  @receiver(post_save,sender=User)
  def createuserprofile(sender, instance, created, **kwargs):
    if created:
      profile.objects.create(user=instance)

  @receiver(post_save, sender=User)
  def saveuserprofile(sender, instance, **kwargs):
      instance.profile.save()
  
  
