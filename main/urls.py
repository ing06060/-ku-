from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ,name='first'),
    path('loginmain/', views.loginmain ,name='loginmain'),
]
