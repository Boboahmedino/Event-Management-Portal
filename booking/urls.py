from django.urls import path
from .import views


urlpatterns = [
    path('select', views.select, name  = 'select'),
    path('contact', views.contact, name= 'contact'),

    
  
    
]
