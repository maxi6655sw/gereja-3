from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def jadwal_misa(request):
    return render(request, 'jadwal_misa.html')

def jadwal_petugas(request):
    return render(request, 'jadwal_petugas.html')