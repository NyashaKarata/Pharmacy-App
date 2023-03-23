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


class EmployeeDetailView(DetailView):
    model = Employee
    context_object_name = "employee"
    template_name = "employee_management/employee/.html"


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
    template_name = "employee_management/employee/.html"
    
    def get_success_url(self) -> str:
        return reverse('list-employees')
