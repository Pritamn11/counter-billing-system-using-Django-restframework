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
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.



class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    authentication_classes = [JWTAuthentication]


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [JWTAuthentication]


class CustomerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [JWTAuthentication]


class CustomerBill(APIView):
    def post(self, request):
        customer_id = request.data.get('customer_id')
        product_id = request.data.get('product_id')
        employee_id = request.data.get('employee_id')

        
        # Retrieve customer
        try:
            customer = Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Retrieve product
        try:
            products = Product.objects.filter(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Retrieve employee
        try:
            employee = Employee.objects.get(id=employee_id)
        except Employee.DoesNotExist:
            return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)


        total_amount = sum(product.price for product in products)

        bill = Bill.objects.create(customer=customer, total_amount=total_amount, created_by=employee)
        bill.products.add(*products)

        serializer = BillSerializer(bill)
        return Response(serializer.data, status=201)



class RegisterUser(APIView):
    def post(self, request):
        serializer = EmployeeSerializer(data = request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status' : 403, 'errors' : serializer.errors, 'message' : 'Validation error. Please check your data.'}) 
        employee = serializer.save()
    
        refresh = RefreshToken.for_user(employee)
        
        return Response({'status' : 200 , 'payload' : serializer.data, 
                        'refresh': str(refresh), 'access': str(refresh.access_token),  
                        'message' : 'your data is saved'})
        

class EmployeeLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        employee = authenticate(username = username, password = password)
        if employee:
            refresh = RefreshToken.for_user(employee)
            return Response({'status' : 200 ,  'refresh': str(refresh), 'access': str(refresh.access_token)})
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)








#     login(request , employee)
#     token, created = Token.objects.get_or_create(user=employee)
#     return Response({'token': token.key}, status=status.HTTP_200_OK)
# else:
#     return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


# @api_view(['POST'])
# def login(request):
#     user = get_object_or_404(Employee, username = request.data['username'])
#     if not user.check_password(request.data['password']):
#         return Response({"detail":"Not found."}, status=status.HTTP_400_BAD_REQUEST)
#     token, created = Token.objects.get_or_create(user=user)
#     serializer = EmployeeSerializer(instance=user)
#     return Response({"token": token.key, "user": serializer.data})

# @api_view(['POST'])
# def test_bill(request):
#     customer_id = request.data.get('customer_id')
#     product_id = request.data.get('product_id')
#     employee_id = request.data.get('employee_id')
    
#     customer = Customer.objects.get(id=customer_id)
#     employee = Employee.objects.get(id=employee_id)


#     products = Product.objects.filter(id=product_id)
    
#     total_amount = sum(product.price for product in products)
    
#     bill = Bill.objects.create(customer=customer, total_amount=total_amount, created_by=employee)
#     bill.products.add(*products)

#     customer_data = CustomerSerializer(customer).data
#     product_data = ProductSerializer(products, many=True).data
#     employee_data = EmployeeSerializer(employee).data
    

#     data = {
#         'id': bill.id,
#         'customer_id': customer_id,
#         'product_ids': product_id,
#         'employee_id': employee_id,
#         'total_amount': total_amount,
#         'generated_at': bill.generated_at 
#     }
#     return Response(data)
