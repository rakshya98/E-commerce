from django.db import models
from datetime import date


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name=models.CharField(max_length=60)
    product_category=models.CharField(max_length=50 , default="Null")
    product_subcategory=models.CharField(max_length=50 , default="Null")
    product_price=models.IntegerField(default=0)
    product_description=models.CharField(max_length=350)
    pub_date=models.DateField(default=date.today)
    image=models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name
    
class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000)
    amount=models.IntegerField(default=0)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    phone=models.CharField(max_length=70,default="")
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)     
    

    

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="") 


class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=500)
    timestamp=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7]+"..."
       