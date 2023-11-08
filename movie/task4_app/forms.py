from django import forms
from .models import Task4

class Task4_form(forms.ModelForm):
    class Meta:
        model = Task4
        fields = ['name','desc','image']