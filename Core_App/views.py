from django.shortcuts import render
from Product_App.models import Products
from Product_App.models import Product_Category
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.db.models import QuerySet
import random


# view function for product display and searching
def home_page(request):
    products = Products.objects.all()
    Category = Product_Category.objects.all()
    searchTerm = request.GET.get('Search_item')
    product_search_result = Products.objects.filter(product_name=searchTerm).all()
    if len(product_search_result) > 0 :
        return render(request,'home.html',{'products': product_search_result,'cat': Category })
    else:
        return render(request,'home.html',{'products': products ,'cat': Category })




