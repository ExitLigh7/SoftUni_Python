from django.contrib import admin
from models_demo.web.models import Employee, NullBlankDemo, Department, Project, Category


# This enables "Employee" model in django admin
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'level')
    list_filter = ('level',)
    search_fields = ('first_name', 'last_name',)

@admin.register(NullBlankDemo)
class NullBlankDemoAdmin(admin.ModelAdmin):
    pass

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass