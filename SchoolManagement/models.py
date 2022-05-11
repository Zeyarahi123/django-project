from django.db import models
from rest_framework import serializers


# Create your models here.
class Registration(models.Model):
    full_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=15)
    email = models.CharField(max_length=20)
    Category = models.CharField(max_length=20)


class Student(models.Model):
    full_name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    mother_name= models.CharField(max_length=15)
    present_class= models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    marks =models.IntegerField()


class RegistrationSerializer(serializers.ModelSerializer):
     class Meta:
         model=Registration
         fields=('full_name','username','password','email','Category')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('full_name','father_name','mother_name','present_class','address','marks')