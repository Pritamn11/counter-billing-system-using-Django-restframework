from rest_framework import serializers
from .models import Product, Employee, Customer, Bill

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['username', 'password', 'email', 'employee_id', 'department', 'position']

    def create(self, validated_data):
        employee = Employee.objects.create(username = validated_data['username'])
        employee.set_password(validated_data['password'])
        employee.save()
        return employee
    

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = "__all__"

