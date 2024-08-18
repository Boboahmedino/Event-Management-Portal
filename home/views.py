import re
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def reservation(request):
    return render(request, 'home/reservation.html')

def makanjuola(request):
    return render(request, 'home/makanjuola.html')

def auditorium(request):
    return render(request, 'home/auditorium.html')