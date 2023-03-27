from employe_management.models.employee import Employee
from form_helpers import SubmitButtonHelper
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Div, ButtonHolder, Submit
from django import forms


class EmployeeForm(forms.ModelForm, SubmitButtonHelper):
    
    
        
        # def __init__(self, *args, **kwargs):
        #     self.helper = FormHelper()
        #     self.helper.layout = Layout(
        #         Div(
        #             Div(Field('first_name'), css_class='col-md-4', ),
        #             Div(Field('last_name'), css_class='col-md-4', ),
        #             Div(Field('employee_code'), css_class='col-md-4', ),
                    
        #             css_class='row',
        #         ),
                
        #         Div(
        #             Div(Field('personal_email'), css_class='col-md-4', ),
        #             Div(Field('work_email'), css_class='col-md-4', ),
        #             Div(Field('phone'), css_class='col-md-4', ),
        #             Div(Field('employment_type'), css_class='col-md-4', ),
        #             Div(Field('job_title'), css_class='col-md-4', ),
        #             css_class='row',
        #         ),
                
                
        #     )
        #     # super(EmployeeForm, self).__init__(*args, **kwargs)
            
        class Meta:
            model = Employee
            fields = '__all__' 
            
            
    
   