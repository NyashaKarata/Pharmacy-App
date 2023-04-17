from django.urls import path
from .views.drugs import drug_delete
from .views.drugs import (DrugCreateView,
                    DrugDetailView,
                    DrugListView,
                    DrugUpdateView)

urlpatterns = [
    path("drug/index/", DrugListView.as_view(), name="list-drugs"),
    path("drug/create/", DrugCreateView.as_view(), name="create-drug"),
    path("drug/detail/<int:pk>/", DrugDetailView.as_view(),name="drug-detail"),
    path("drug/update/<int:pk>/", DrugUpdateView.as_view(), name="update-drug"),
    path("drug/delete/<int:pk>/", drug_delete,name="delete-drug"),
]