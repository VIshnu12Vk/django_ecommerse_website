from django.db import models

# Create your models here.
from django.db import models

class Product_Category(models.Model):
    cat_id = models.AutoField(primary_key=True)  
    cat_name = models.CharField(max_length=100, unique=True)
    cat_image = models.ImageField(upload_to='Product_App/media/',null=True)

    def __str__(self):
        return self.cat_name

class Products(models.Model):
    product_id = models.AutoField(primary_key=True) 
    product_name = models.CharField(max_length=100,null=False)
    product_image = models.ImageField(upload_to='Product_App/media/')
    cat_id = models.ForeignKey(Product_Category, on_delete=models.CASCADE) 
    marginal_price = models.IntegerField()
    orginal_price = models.IntegerField()
    stock = models.IntegerField()
    company = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    weight = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    material = models.CharField(max_length=50,null=True)
    


    def __str__(self):
        return self.product_name
# mydata = Member.objects.filter(firstname='Emil').values()