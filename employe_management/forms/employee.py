from employe_management.models import Employee
from form_helpers import SubmitButtonHelper
from django import forms


class KeyForm(forms.ModelForm, SubmitButtonHelper):
    
    class Meta:
        model = Employee
        fields = '__all__'
    
   