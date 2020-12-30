from rest_framework import serializers

from api.models import Service, Category, Employee


class ServiceListSerializer(serializers.ModelSerializer):
    """Список услуг"""

    class Meta:
        model = Service
        fields = ("id", "title", "price")


class ServiceDetailSerializer(serializers.ModelSerializer):
    """Информация об услуге"""

    class Meta:
        model = Service
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """
    Вывод списка категорий,
    Вывод информации об одной категории
    """

    class Meta:
        model = Category
        fields = '__all__'


class EmployeeListSerializer(serializers.ModelSerializer):
    """Список сотрудников"""

    class Meta:
        model = Employee
        fields = ('id', 'name', 'position', 'photo')


class EmployeeDetailSerializer(serializers.ModelSerializer):
    """Инофрмация о сотруднике"""

    class Meta:
        model = Employee
        fields = '__all__'
