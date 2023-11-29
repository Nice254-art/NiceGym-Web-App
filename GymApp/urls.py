
from django.contrib import admin
from django.urls import path
from GymApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('classes/', views.classes, name='classes'),
    path('contact/', views.contact, name='contact'),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('book/', views.book, name='book'),
    path('success/', views.success, name='success'),

]
