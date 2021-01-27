from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image= models.ImageField(upload_to="shop/images",default="")


    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50 , default="")
    phone = models.CharField(max_length=70, default="")
    address=models.CharField(max_length=150,default="")



    def __str__(self):
        return self.name

#
# class Login(models.Model):
#     msg_id = models.AutoField(primary_key=True)
#     email= models.CharField(max_length=70 , default="")
#     password = models.CharField(max_length=70, default="")

    #
    # def __str__(self):
    #     return self.email




