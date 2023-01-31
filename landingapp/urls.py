from django.urls import path
from landingapp import views

urlpatterns =[
  path('',views.index,name='index'),
]