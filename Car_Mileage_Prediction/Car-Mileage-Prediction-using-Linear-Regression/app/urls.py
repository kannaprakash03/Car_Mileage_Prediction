from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict, name='predictpage'),
    path('predictMileage', views.predictMileage, name='predictMileage'),
]
