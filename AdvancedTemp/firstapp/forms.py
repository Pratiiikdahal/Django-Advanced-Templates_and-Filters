from django import forms
from firstapp.models import *


class empForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields= '__all__'