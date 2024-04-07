from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'email', 'employee_id', 'department','position')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','description', 'price', 'quantity')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'phone_number', 'gender', 'age', 'address')

class BillAdmin(admin.ModelAdmin):
    list_display = ('customer','get_product_names', 'total_amount', 'created_by', 'generated_at')
    def get_product_names(self, obj):
        return ', '.join([product.name for product in obj.products.all()])

    get_product_names.short_description = 'Products'


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Customer, CustomerAdmin)    
admin.site.register(Product, ProductAdmin)    
admin.site.register(Bill, BillAdmin)
