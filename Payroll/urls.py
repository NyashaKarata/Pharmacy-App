from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('employee-management/', include('employee_management.urls')),
    
]
