from employe_management.models.employee import Employee
from form_helpers import SubmitButtonHelper
from django import forms


class EmployeeForm(forms.ModelForm, SubmitButtonHelper):
    
    class Meta:
        model = Employee
        fields = '__all__'
    
   