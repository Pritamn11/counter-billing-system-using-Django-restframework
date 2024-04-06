from django.urls import path 
from . import views 
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [
    path('products/', views.ProductListCreateAPIView.as_view(), name='products'),
    path('products/<int:pk>', views.ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-info'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='sagger-ui'),
    path('api/schema/redoc', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('customer/<int:pk>', views.CustomerRetrieveUpdateDestroyAPIView.as_view(), name='customer'),
    path('bill/', views.CustomerBill.as_view(), name='bill'),
    
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.EmployeeLogin.as_view(), name='login'),
    
]

