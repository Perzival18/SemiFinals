from django.urls import path
from . import views

app_name = 'covid'

urlpatterns = [
 path('', views.home, name='home'),
 path('covidtracker/', views.patient, name='covidtracker'),


]