from django.shortcuts import render
from django.http import HttpResponse
from django101.tasks.models import Task


def bare_minimum_view(request):
    return render(request, 'index.html')

def show_all_tasks(request):
    all_tasks = Task.objects.all()
    result = '; '.join(f'{t.name}({t.id})' for t in all_tasks)
    return HttpResponse(result)

def index(request):
    context = {
        'title': 'The tasks app!',
        'tasks': Task.objects.all(),
    }
    return render(request, 'index.html', context)