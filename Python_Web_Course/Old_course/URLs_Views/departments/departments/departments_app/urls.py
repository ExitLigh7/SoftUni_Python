from django.urls import path

from departments.departments_app.views import show_departments, show_department_by_id, show_department_by_name

urlpatterns = (
    path('', show_departments, name= 'show_departments'),
    path('find_by_id/<int:department_id>/', show_department_by_id, name='department_by_id'),
    path('<str:department_name>/',show_department_by_name)
)

