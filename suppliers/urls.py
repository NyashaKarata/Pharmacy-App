from django.urls import path

from .views.suppliers import (SupplierCreateView,
                    SupplierDeleteView, 
                    SupplierDetailView,
                    SupplierListView,
                    SupplierUpdateView)

urlpatterns = [
    path("supplier/index/", SupplierListView.as_view(), name="list-suppliers"),
    path("supplier/create/", SupplierCreateView.as_view(), name="create-supplier"),
    path("supplier/detail/<int:pk>/", SupplierDetailView.as_view(),name="supplier-detail"),
    path("supplier/update/<int:pk>/", SupplierUpdateView.as_view(), name="update-supplier"),
    path("supplier/delete/<int:pk>/", SupplierDeleteView.as_view(),name="delete-supplier"),
]