from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api import serializers
from api import models


class BusinessClientViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.BusinessClientSerializer
    queryset = models.BusinessClient.objects.all()


class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ClientSerializer
    queryset = models.Client.objects.all()


class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.EmployeeSerializer
    queryset = models.Employee.objects.all()


class PersonalAppointmentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.PersonalAppointmentSerializer
    queryset = models.PersonalAppointment.objects.all()


class BusinessAppointmentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.BusinessAppointmentSerializer
    queryset = models.BusinessAppointment.objects.all()


class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CompanySerializer
    queryset = models.Company.objects.all()
