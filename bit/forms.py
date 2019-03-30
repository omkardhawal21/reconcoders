from django import forms

from .models import login

class Loginform(forms.ModelForm):
    class Meta:
        model = login
        fields = ["username", "password"]