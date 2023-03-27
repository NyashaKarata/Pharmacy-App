from django.shortcuts import render, reverse
from employe_management.forms.employee import EmployeeForm
from employe_management.models.employee import Employee
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView,
)
class EmployeeListView(ListView):
    model = Employee
    context_object_name = "employee"
    template_name = "employee_management/employee/list.html"


class EmployeeCreateView(CreateView):
    model = Employee
    context_object_name = "employee"
    form_class = EmployeeForm
    template_name = "employee_management/employee/create.html"
 
    def get_success_url(self) -> str:
        return reverse('list-employees')    


class PersonalInfoDetailView(DetailView):
    model = Employee
    context_object_name = "employee"
    template_name = "employee_management/employee/personalDetail.html"
    
class WorkInfoDetailView(DetailView):
    model = Employee
    context_object_name = "employee"
    template_name = "employee_management/employee/workDetail.html"
    
class PayrollInfoDetailView(DetailView):
    model = Employee
    context_object_name = "employee"
    template_name = "employee_management/employee/payrollDetail.html"


class EmployeeUpdateView(UpdateView):
    model = Employee
    context_object_name = "employee"
    form_class = EmployeeForm
    template_name = "employee_management/employee/update.html"
    
    def get_success_url(self) -> str:
        return reverse('list-employees') 
    
    
class EmployeeDeleteView(DeleteView):
    model = Employee
    context_object_name = "employee"
    template_name = "employee_management/employee/delete.html"
    
    def get_success_url(self) -> str:
        return reverse('list-employees')
