from django.shortcuts import render
from .geo import foo

def login(request):
    return render(request,"login.html",{})


def patient(request):
    return render(request,"patient.html",{})


def doctor(request):
    return render(request,"doctor.html",{})

def patientdash(request):
    return render(request,"patientdash.html",{})

def doctordash(request):
    return render(request,"doctordash.html",{})

def default_map(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    co=foo()
    return render(request, 'default.html', {'mapbox_access_token': mapbox_access_token,'co':co})
