from django.shortcuts import render, get_object_or_404, redirect

from models_demo.web.models import Employee, Department


def index(request):
    # # this will be query set, it needs to be used in order to view some result.("lazy")
    # employees = Employee.objects.all()

    context = {
        'employees': Employee.objects.all(),
        'employees2' : Employee.objects.filter(department_id =1),
        # .order_by('last_name', 'first_name'),
        #  department can be reached also with: .filter(department__name='Engineering')
        'department': Department.objects.get(pk=1),
    #    objects.get returns single object! (not a query set) it's "eager"
    }

    return render(request, 'index.html', context)

def department_details(request, pk, slug):
    context = {
        'department': get_object_or_404(Department, pk=pk, slug=slug),
    }
    return render(request, 'department_details.html', context)

def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    # delete is "eager"!
    return redirect('index')


# # Project.objects.all() \
# .delete()                          - will delete all projects

# Project.objects.filter() \
#     .delete()                      - will delete only projects matching the filter