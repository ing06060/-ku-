from django.urls import path
from . import views

app_name='lecture' 

urlpatterns = [
    path('search/', views.form_test, name='search'),
    path('result/',views.form_test, name='result'),
]