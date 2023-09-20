from django.shortcuts import render
from Product_App.models import Products
from Product_App.models import Product_Category
from django.shortcuts import render, get_object_or_404

# view function for product detailed view
def product_detail_view(request, product_id):
    product = get_object_or_404(Products, product_id=product_id)
    category=Products.objects.filter(cat_id= product.cat_id).all()
    # products_list = Products.objects.filter(product_id=product_id).all()
    context = {'product': product , 'product_obj':  category}
    return render(request, 'products_detail.html', context)

# view function for displaying products based on category
def category_products_list(request,cat_id):
    # product_cat = get_object_or_404(Products, cat_id=category_id)
    product_cat = Products.objects.filter(cat_id=cat_id).all()
    context = {'Product_cat': product_cat}
    return render(request,'cat_product_list.html', context)