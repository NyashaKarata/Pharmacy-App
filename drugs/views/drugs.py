from django.shortcuts import get_object_or_404, redirect, render, reverse
from drugs.models.drug import Drug
from django.http import HttpResponseRedirect
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    DeleteView,
  
)
class DrugListView(ListView):
    model = Drug
    context_object_name = "drugs"
    template_name = "drugs/list.html"


class DrugCreateView(TemplateView):
    model = Drug
    template_name = "drugs/create.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        drugs = Drug.objects.all()
        context["drugs"] = drugs
        
        return context
    
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            name = request.POST.get('name')
            date_supplied = request.POST.get('date_supplied')
            price = request.POST.get('price')
            strength = request.POST.get('strength')
            quantity = request.POST.get('quantity')
            expiry_date = request.POST.get('expiry_date')
            
            drugModel = Drug()
            drugModel.name = name
            drugModel.date_supplied = date_supplied
            drugModel.price = price
            drugModel.quantity = quantity
            drugModel.strength = strength
            drugModel.expiry_date = expiry_date
            drugModel.save()
            
            return HttpResponseRedirect(reverse('list-drugs'))
        return render(request, self.template_name)
    
 
    def get_success_url(self) -> str:
        return reverse('list-drugs')    


def drug_delete(request, pk):
    drug = get_object_or_404(Drug, pk=pk)

    if request.method == 'POST':
        drug.delete()
        return redirect('list-drugs')

    return render(request, 'drugs/delete.html', {'object': drug})

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
