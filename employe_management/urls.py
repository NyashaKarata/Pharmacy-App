from django.urls import path

from .views.employee import (EmployeeCreateView,
                    EmployeeDeleteView, 
                    PersonalInfoDetailView,
                    WorkInfoDetailView,
                    PayrollInfoDetailView,
                    EmployeeListView,
                    EmployeeUpdateView)

urlpatterns = [
    path("employee/index/", EmployeeListView.as_view(), name="list-employees"),
    path("employee/create/", EmployeeCreateView.as_view(), name="create-employee"),
    path("employee/detail/<int:pk>/",PersonalInfoDetailView.as_view(),name="detail-employee"),
    path("employee/workinfo/detail/<int:pk>/",WorkInfoDetailView.as_view(),name="workinfo-employee"),
    path("employee/payrollinfo/detail/<int:pk>/",PayrollInfoDetailView.as_view(),name="payrollinfo-employee"),
    path("employee/update/<int:pk>/", EmployeeUpdateView.as_view(), name="update-employee"),
    path("employee/delete/<int:pk>/", EmployeeDeleteView.as_view(),name="delete-employee"),
]