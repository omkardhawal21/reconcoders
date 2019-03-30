from mapbox import Geocoder
from .models import Doctor
def foo():
	a=Doctor.objects.all()
	b=[]
	coordinates=[]
	for i in range(len(a)):
		b.append(a[i].doctor_address)
	geocoder=Geocoder(access_token="pk.eyJ1Ijoib21rYXIyMSIsImEiOiJjanRxc3hoamcwZDNtNGRxZGNnaXF2ZHU3In0.Ovq0lb6DSdnLkIMMb32UPA")
	for i in range(len(b)):
		response=geocoder.forward(b[i])
		collection=response.json()
		coordinates.append(collection['features'][0]['center'][0])
		coordinates.append(collection['features'][0]['center'][1])
	coordinates=[-0.118092,51.509865]
	return(coordinates)