from django.shortcuts import render
from rest_framework.permissions import AllowAny,IsAuthenticated
from Employee.models import *
from .serializers import *
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView

class EmployeeRegisterAPIView(CreateAPIView):
    permission_classes=[AllowAny]
    serializer_class = RegisterEmployeeSerializer
    queryset = Employee.objects.all()