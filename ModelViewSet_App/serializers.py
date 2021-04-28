
from rest_framework import serializers
from .models import Employee

# This code addedd from Pycharm to Github.
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'