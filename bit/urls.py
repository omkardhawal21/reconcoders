from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.login, name='login'),
    path('patient/', views.patient, name='patient'),
    path('doctor/', views.doctor, name='doctor'),
    path('patientdash/', views.patientdash, name='patientdash'),
    path('doctordash/', views.doctordash, name='doctordash'),
    path('disease/', views.disease, name='disease'),
]
