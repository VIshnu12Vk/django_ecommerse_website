from django.contrib import admin
from .models import Products,Product_Category
# Register your models here.
admin.site.register(Product_Category)
admin.site.register(Products)
