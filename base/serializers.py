from rest_framework import serializers
from .models import Product, Employee, Customer, Bill
from django.contrib.auth import get_user_model
User = get_user_model()


class EmployeeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'employee_id', 'department', 'position']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        employee = User.objects.create(**validated_data)
        if password is not None:
            employee.set_password(password)
            employee.save()
        return employee



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
    

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = "__all__"

















# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = ['username', 'password', 'email', 'employee_id', 'department', 'position']

#     def create(self, validated_data):
#         employee = Employee.objects.create(username = validated_data['username'])
#         employee.set_password(validated_data['password'])
#         employee.save()
#         return employee