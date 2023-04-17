from django.shortcuts import render, reverse
from suppliers.models.supplier import Supplier
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    DeleteView,
  
)
class SupplierListView(ListView):
    model = Supplier
    context_object_name = "supplier"
    template_name = "suppliers/list.html"


class SupplierCreateView(TemplateView):
    model = Supplier
    context_object_name = "supplier"
    template_name = "suppliers/create.html"
 
    def get_success_url(self) -> str:
        return reverse('list-Suppliers')    


class SupplierDetailView(DetailView):
    model = Supplier
    context_object_name = "supplier"
    template_name = "suppliers/detail.html"


class SupplierUpdateView(TemplateView):
    model = Supplier
    context_object_name = "supplier"
    template_name = "suppliers/update.html"
    
    def get_success_url(self) -> str:
        return reverse('list-suppliers') 
    
    
class SupplierDeleteView(DeleteView):
    model = Supplier
    context_object_name = "Supplier"
    template_name = "suppliers/delete.html"
    
    def get_success_url(self) -> str:
        return reverse('list-suppliers')
