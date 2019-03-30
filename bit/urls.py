from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path('', views.login, name='login'),
    path('patient/', views.patient, name='patient'),
    path('doctor/', views.doctor, name='doctor'),
    path('patientdash/', views.patientdash, name='doctor'),
    path('doctordash/', views.doctordash, name='doctor'),
    path('map/', views.default_map, name="default")
]
