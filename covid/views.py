from django.shortcuts import render, get_object_or_404
from .models import Patient

# Create your views here.

def home(request):
    return render(request, 'covid19/home.html')

def patient(request):
    patients = Patient.objects.all()
    return render(request, 'covid19/covidtracker.html', {'patients': patients})