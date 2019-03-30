from django.contrib import admin

from .models import Patient
from .models import Doctor
from .models import Disease
from .models import Login


admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Disease)
admin.site.register(Login)