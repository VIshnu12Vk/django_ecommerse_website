from django.urls import path 
from . import views

urlpatterns = [
    path('add_cart/<int:id>/',views.insert_into_cart,name="add_cart"),
    path('cart_listing/',views.cart_display,name="cart"),
    path('cart_remove/<str:p_name>',views.cart_remove,name="remove_cart_item"),
]
