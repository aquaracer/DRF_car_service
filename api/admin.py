from django.contrib import admin

from api.models import Service, Employee, Category


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class EmployeeAdmin(admin.ModelAdmin):
    pass
