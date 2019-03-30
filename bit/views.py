from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from bit.forms import Loginform
from bit.models import Doctor, Disease, Patient


def login(request):
    if request.method == 'POST':
        form = Loginform(request.POST or None)
        if form.is_valid():
            form.save()
            # messages.success(request,('List has been updated'))
            user = form.cleaned_data['username']
            passw = form.cleaned_data['password']
            try:
                all_items = Doctor.objects.get(doctor_username=user)
                named = all_items.doctor_name
                # print(info)
                # all_items = go

                return render(request, "doctordash.html", {'all_items': all_items})
            except ObjectDoesNotExist:
                go = None
                try:
                    pat = Patient.objects.get(patient_username=user)
                    all_items = pat
                    infop = Disease.objects.filter(patient=all_items.patient_name)
                    print(infop)
                    return render(request, "patientdash.html", {'all_items': all_items,'infop':infop})
                except ObjectDoesNotExist:
                    pat = None
            #return render(request, "login.html", {'form': form})
    return render(request, "login.html", {})




def patient(request):
    return render(request,"patient.html",{})


def doctor(request):
    return render(request,"doctor.html",{})

def patientdash(request):
    return render(request,"patientdash.html",{})

def doctordash(request):
    return render(request,"doctordash.html",{})

