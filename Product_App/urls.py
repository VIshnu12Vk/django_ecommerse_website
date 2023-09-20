from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:product_id>/', views.product_detail_view, name='product_detail'),
    path('category_list/<int:cat_id>/',views.category_products_list,name="category_listing"),
]
