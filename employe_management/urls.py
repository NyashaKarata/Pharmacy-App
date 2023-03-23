from django.urls import path

from .views.employee import (EmployeeCreateView,
                    EmployeeDeleteView, 
                    EmployeeDetailView,
                    EmployeeListView,
                    EmployeeUpdateView)

urlpatterns = [
    path("employee/index/", EmployeeListView.as_view(), name="list-employees"),
    path("employee/create/", EmployeeCreateView.as_view(), name="create-employee"),
    path("employee/detail/<int:pk>/",EmployeeDetailView.as_view(),name="detail-employee"),
    path("employee/update/<int:pk>/", EmployeeUpdateView.as_view(), name="update-employee"),
    path("employee/delete/<int:pk>/", EmployeeDeleteView.as_view(),name="delete-employee"),
]