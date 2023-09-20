from django.db import models
from django.contrib.auth.models import User

class User_Info(models.Model):
   user_name = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
   user_img = models.ImageField(upload_to='User_Profile_App/media/',null=True)
   address = models.CharField(max_length=100,null=True)
   email = models.CharField(max_length=100,null=True)
   phone = models.CharField(primary_key=True,max_length=50,null=False)
   alt_phone = models.CharField(max_length=100,null=True)
   gender = models.CharField(max_length=100,null=True)
   pincode = models.IntegerField(null=True)
  