from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

DEPARTMENTS = {
    'marketing': 1,
    'sales': 2,
    'hr': 3,
    'it': 4,
}

def show_departments(request):
    return HttpResponse('Departments are under construction')

# def show_department_by_id(request, department_id):
#     if department_id == 1:
#         department_name = "Developers"
#     elif department_id == 2:
#         department_name = "Trainers"
#     html = "<html><body><h1>" \
#            "Department Name: %s, Department ID: %s" \
#            "</h1></body></html>" \
#            % (department_name, department_id)
#     return HttpResponse(html)

def show_department_by_id(request, department_id):
    context = {"department_name": "marketing",
               "department_id": department_id}
    return render(
        request=request,
        template_name='department_by_id.html',
        context=context,
    )


def show_department_by_name(request, department_name):
    return redirect('show_departments')