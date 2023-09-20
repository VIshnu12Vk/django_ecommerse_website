from django.db import models
from User_Profile_App.models import User_Info
from Product_App.models  import Products

# Create your models here.
class Cart(models.Model):
    user_phone= models.ForeignKey(User_Info,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    count = models.IntegerField(null=True)

    def __str__(self):
        return self.product_id