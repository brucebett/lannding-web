from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('service_details/', views.service_details, name='service_details'),
    
]
