from turtle import update

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.db import connection
from .models import Student,Registration
from .models import StudentSerializer, RegistrationSerializer
from rest_framework import serializers



def Login(request):

    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            Category = request.POST['Category']
            user = auth.authenticate(username=username, password=password)

            if Category=="Student":
                auth.login(request, user)
                return redirect("Student.html")  # it will redirect to student.html
            elif Category=="Teacher":
                auth.login(request, user)
                return redirect("Add_student.html")   # it will redirect to teacher.html
            elif Category=="Admin":
                auth.login(request, user)
                return redirect("Admin.html")     # it will redirect to admin.html
            else:
                messages.info(request, "Invalid User_Name or Password")
                return redirect('Login')

    else:
        return render(request, "Login.html")


def Registration(request):
     if request.method == 'POST':
          full_name = request.POST['full_name']
          username = request.POST['username']
          password = request.POST['password1']
          password1 = request.POST['password2']
          email = request.POST['email']
          Category= request.POST['Category']

          #we are checking wheather password1 is same as password2 or nor(password1==password2)

          if password == password1:
               if User.objects.filter(username=username).exists():  # it will check wheather same username is available or not in database
                     #print("User_Name is already available") #it will print on terminal
                      messages.info(request,'User_Name is already taken')  #it will give message on same form
                      return redirect('Registration') #it will send again to register form

               elif User.objects.filter(email=email).exists():  #it will check same email is available in database or not
                     #print("Email is already available")    #it will print on terminal
                     messages.info(request, 'Email is already taken') #it will give message on same form
                     return redirect('Registration') # it will send again to register form

               else:
                     user=User.objects.create_user(full_name=full_name, username=username, password=password, email=email, Category=Category)
                     user.save();
                     #print("Created SuccessFully")    #it will print on terminal
                     messages.info(request, 'User Created SuccessFully')   #it will give message on same form
                     return redirect("Login")
          else:
               #print("Password Not Matching")   #it will print on terminal
               messages.info(request, 'Password is Not Matching')  #it will give message on same form
               return redirect('Registration')   # it will send again to registration form
     else:

          return render(request, "Registration.html")



def Student(request):
    Student_data=Student.objects.filter(full_name="full_name")
    return render(request,'Student.html',{'Students': Student_data})



def Add_student(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        father_name = request.POST['father_name']
        mother_name= request.POST['mother_name']
        present_class = request.POST['present_class']
        address= request.POST['address']
        marks = request.POST['marks']

        cursor = connection.cursor()
        Query1 = "insert into SchoolManagement_Student(full_name,father_name,mother_name,present_class,address,marks) values (%s,%s,%s,%s,%s,%i)"
        value = ('full_name','father_name','mother_name','present_class','Address','marks')
        cursor.execute(Query1, value)
        messages.info(request, 'Details is inserted Successfully')
        return redirect('Add_student')

    else:
        return redirect(request,'Add_student.html')


class StudentSerializers(serializers.ModelsSerializer):
    queryset=Registration.object.all()
    serializer_class=StudentSerializer


class RegistrationSerializers(serializers.ModelSerializer):

    queryset1=Registration.object.all()
    serializer_class=RegistrationSerializer


def Forgot(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        password1 = request.POST['password2']
        email = request.POST['email']


        # we are checking wheather password1 is same as password2 or nor(password1==password2)

        if password == password1:
            if User.objects.filter(username=username).exists():  # it will check wheather same username is available or not in database
                # print("User_Name is already available") #it will print on terminal
                  messages.info(request, 'User_Name is already taken')  # it will give message on same form
                  return redirect('ForgotPassword')  # it will send again to register form

            elif User.objects.filter(email=email).exists():  # it will check same email is available in database or not
                  # print("Email is already available")    #it will print on terminal
                   messages.info(request, 'Email is already taken')  # it will give message on same form
                   return redirect('ForgotPassword')  # it will send again to register form

            else:
                query = User.objects.filter(email='email')
                if email===query:
                    update user set password="password" where email="email"
                    query.save();
               # print("Created SuccessFully")    #it will print on terminal
                    messages.info(request, 'Updated Sucessfully')  # it will give message on same form
                    return redirect("Login")

    else:

       return render(request, "ForgotPassword.html")


