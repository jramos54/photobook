
from django.urls import path
from imageapp import views

urlpatterns=[
  path('newcategory/',views.newcategory,name='newcategory'),
  path('addimage/',views.addimage,name='addimage'),
  path('categorydetail/<slug:slug>',views.categorydetail,name='categorydetail'),
  path('imagedetail/<slug:slug1>/<slug:slug2>',views.imagedetail,name='imagedetail')
]