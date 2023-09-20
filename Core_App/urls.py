from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('products/',views.home_page,name='products'),
    path('/',include('User_Profile_App.urls'),name=''),
    path('/',include('Product_App.urls'),name=''),
    path('/',include('Cart_App.urls'),name=''),
    path('/',include('Order_App.urls'),name=''),
]
