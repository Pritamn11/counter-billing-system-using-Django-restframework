from django.shortcuts import render
from rest_framework import generics
from .models import Product, Employee, Customer, Bill
from .serializers import ProductSerializer, EmployeeSerializer, CustomerSerializer, BillSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
# Create your views here.


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class CustomerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]


class CustomerBill(APIView):
    def post(self, request):
        customer_id = request.data.get('id')
        product_id = request.data.get('product_id')
        employee_id = request.data.get('employee_id')

        
        # Retrieve customer
        try:
            customer = Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Retrieve product
        try:
            product = Product.objects.filter(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Retrieve employee
        try:
            employee = Employee.objects.get(id=employee_id)
        except Employee.DoesNotExist:
            return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)


        total_amount = sum(product.price for product in product)

        bill = Bill.objects.create(customer=customer, total_amount=total_amount, employee_id=employee.id)
        bill.products.add(*product)

        serializer = BillSerializer(bill)
        return Response(serializer.data, status=201)



class RegisterUser(APIView):
    def post(self, request):
        serializer = EmployeeSerializer(data = request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status' : 403, 'errors' : serializer.errors, 'message' : 'Validation error. Please check your data.'}) 
        employee = serializer.save()
    
        token_obj , _ = Token.objects.get_or_create(user=employee)
        
        return Response({'status' : 200 , 'payload' : serializer.data, 'token': str(token_obj), 'message' : 'your data is saved'})
        

class EmployeeLogin(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        employee = authenticate(username = username, password = password)
        if employee:
            login(request , employee)
            token, created = Token.objects.get_or_create(user=employee)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# @api_view(['POST'])
# def login(request):
#     user = get_object_or_404(Employee, username = request.data['username'])
#     if not user.check_password(request.data['password']):
#         return Response({"detail":"Not found."}, status=status.HTTP_400_BAD_REQUEST)
#     token, created = Token.objects.get_or_create(user=user)
#     serializer = EmployeeSerializer(instance=user)
#     return Response({"token": token.key, "user": serializer.data})

        
