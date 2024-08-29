from django.template import Library

from demo_templates.ts_demo.views import Student

register = Library()

# Simple tag always returns string!
@register.simple_tag(name='student_info')
def show_student_info(student: Student):
    return f"Hello, My name is {student.name} and I am {student.age} years old."


@register.inclusion_tag('tags/nav.html', name='app_nav')
def generate_nav(*args):
    context = {'url_names': args}
    return context
