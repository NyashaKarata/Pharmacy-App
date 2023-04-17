from django.shortcuts import render, reverse
from drugs.models.drug import Drug
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    DeleteView,
  
)
class DrugListView(ListView):
    model = Drug
    context_object_name = "drug"
    template_name = "drugs/list.html"


class DrugCreateView(TemplateView):
    model = Drug
    context_object_name = "drug"
    template_name = "drugs/create.html"
 
    def get_success_url(self) -> str:
        return reverse('list-drugs')    


class DrugDetailView(DetailView):
    model = Drug
    context_object_name = "drug"
    template_name = "drugs/detail.html"


class DrugUpdateView(TemplateView):
    model = Drug
    context_object_name = "drug"
    template_name = "drugs/update.html"
    
    def get_success_url(self) -> str:
        return reverse('list-drugs') 
    
    
class DrugDeleteView(DeleteView):
    model = Drug
    context_object_name = "drug"
    template_name = "drugs/delete.html"
    
    def get_success_url(self) -> str:
        return reverse('list-drugs')
