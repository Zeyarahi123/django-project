
from rest_framework import serializers
from .models import Student,Registration


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['full_name', 'username', 'password', 'email', 'Category']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['full_name', 'father_name', 'mother_name', 'present_class', 'address', 'marks']