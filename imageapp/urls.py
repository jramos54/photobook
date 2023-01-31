from django.urls import path
from imageapp import views

urlpatterns=[
  path('newcategory/',views.newcategory,name='newcategory'),
  path('addimage/',views.addimage,name='addimage')
]