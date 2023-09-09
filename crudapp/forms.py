from django import  forms
from . models import student

class student_form(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'
