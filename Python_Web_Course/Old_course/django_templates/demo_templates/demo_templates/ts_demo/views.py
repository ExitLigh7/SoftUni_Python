import random
from datetime import datetime
from tkinter import IntVar

from django.shortcuts import render, redirect


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"


def index(request):
    context = {
        'title': "softUni Home Page",
        'value': random.random(),
        'info': {
            'address': 'Sofia'
        },
        'student': Student("Ivan", 25),

        'student_info': Student("Ivan", 25).get_info(),
        'now': datetime.now(),
        'students': ['Pesho', "Gosho", "Maria", "Ivan"],
        'values': list(range(20)),
    }

    return render(request, 'index.html', context)

def redirect_to_home(request):
    return redirect('index')

def show_about(request):
    return render(request, 'about.html')
