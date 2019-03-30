from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from bit.forms import Loginform, Diseaseform,  Patientform, Doctorform
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
                request.session['dname'] = named
                info = Disease.objects.filter(doctor=named)
                # print(info)
                # all_items = go

                return render(request, "doctordash.html", {'all_items': all_items,'info':info})
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
	if request.method == 'POST':
		form = Patientform(request.POST or None)
		if form.is_valid():
			form.save()
			user = request.session['dname']
			patientlist = Patient.objects.all()
			return render(request, "disease.html", {'patientlist':patientlist,'doctor_name': user})
	return render(request, "patient.html", {})


def doctor(request):
	if request.method == 'POST':
		form = Doctorform(request.POST or None)
		if form.is_valid():
			form.save()
			return render(request, "login.html", {})
	return render(request,"doctor.html",{})

def patientdash(request):
    return render(request,"patientdash.html",{})

def doctordash(request):
	if (request.GET.get('mybtn')):
		user =request.session['dname']
		print(user)
		patientlist = Patient.objects.all()
		return render(request,"disease.html", {'patientlist':patientlist,'doctor_name':user})

def disease(request):
	if request.method == 'POST':
		patientlist = Patient.objects.all()
		form = Diseaseform(request.POST or None)
		if form.is_valid():
			dname = form.cleaned_data['doctor']
			form.save()
			user = request.session['dname']
			all_items = Doctor.objects.get(doctor_username=user)
			named=all_items.doctor_name
			info=Disease.objects.filter(doctor=named)
			return render(request,"doctordash.html",{'all_items': all_items,'info':info})
	return render(request,"disease.html",{})