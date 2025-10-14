from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('jadwal_misa/', views.jadwal_misa, name='jadwal_misa'),
    path('jadwal_petugas/', views.jadwal_petugas, name='jadwal_petugas'),
]
