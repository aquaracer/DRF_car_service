from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from .models import Service, Category, Employee
from .serializers import (ServiceListSerializer,
                          ServiceDetailSerializer,
                          CategorySerializer,
                          EmployeeListSerializer,
                          EmployeeDetailSerializer)


class ServiceViewSet(viewsets.ModelViewSet):
    """CRUD информации об услуге"""

    queryset = Service.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = ['employee', 'category']
    ordering_fields = ['price', 'title']

    def get_serializer_class(self):
        if self.action == 'list':
            return ServiceListSerializer
        else:
            return ServiceDetailSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """CRUD категории"""

    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class EmployeeViewSet(viewsets.ModelViewSet):
    """CRUD информации о сотруднике"""

    queryset = Employee.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return EmployeeListSerializer
        else:
            return EmployeeDetailSerializer
