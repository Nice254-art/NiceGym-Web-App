
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('GymApp.urls')), # ADDING THE URLS IN MY APP TO BE INCLUDED IN MY PROJECT
]
