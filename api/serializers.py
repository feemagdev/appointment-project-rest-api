from rest_framework import serializers
from .models import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class BusinessClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessClient
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class PersonalAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalAppointment
        fields = '__all__'


class BusinessAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessAppointment
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
