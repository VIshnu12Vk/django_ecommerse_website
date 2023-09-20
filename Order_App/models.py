from django.db import models
from User_Profile_App.models import User_Info
from Product_App.models import Products
# Create your models here.
class Buy_history(models.Model):
    phone = models.ForeignKey(User_Info,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    count = models.IntegerField()