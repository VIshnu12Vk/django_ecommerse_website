from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from Cart_App.models import Cart
from User_Profile_App.models import User_Info
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect
from Product_App.models import Products
from Core_App.views import home_page
import random
from django.contrib.auth.decorators import login_required

# view function for inserting products items in the cart
@login_required
def insert_into_cart(request,id):
    user_id = request.user.id
    user_p = get_object_or_404(User_Info, user_name=user_id)
    user_info_instance = User_Info.objects.get(phone=user_p.phone)
    product_instance = Products.objects.get(product_id=id)
    cart = Cart(user_phone=user_info_instance, product_id=product_instance , count=10)
    cart.save()
    return HttpResponse(home_page(request))

# view function for displaying user cart items
@login_required
def cart_display(request):
    user_id = request.user.id
    user_p = get_object_or_404(User_Info, user_name=user_id)
    d = list()
    cat_obj = Cart.objects.filter(user_phone=user_p.phone).all()
    for c in cat_obj:
        d.append(Products.objects.get(product_name=c.product_id))
    if(len(d) == 0):
        suggest_product_list = Products.objects.all()[:3]
    else:
        random_item = random.choice(d)
        suggest_product_cat = Products.objects.filter(product_name=random_item).values('cat_id')
        suggest_product_list = Products.objects.filter(cat_id=suggest_product_cat[0]["cat_id"]).all()[:3]
    context = {'cart_deatil':d ,'sug': suggest_product_list}
    return render(request,"cart.html",context)

# view function for removing items from cart
@login_required
def cart_remove(request, p_name):
    p = Products.objects.filter(product_name=p_name).values('product_id')
    for product in p:
        Cart.objects.filter(product_id=product['product_id']).delete()
    return redirect('products')