

from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import viewsets

class EmplyeeModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer