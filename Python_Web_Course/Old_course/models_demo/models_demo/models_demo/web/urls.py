from django.urls import path
from models_demo.web.views import index, delete_employee, department_details

urlpatterns = [
    path ( '', index, name='index' ),
    path('delete/<int:pk>/', delete_employee, name='delete employee'),
    path('department/<int:pk>/<slug:slug>', department_details, name='department details'),
]