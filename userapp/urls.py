from django.urls import path
from userapp import views

urlpatterns=[
  path('login/',views.login,name='login'),
  path('newuser/',views.newuser,name='newuser')
]