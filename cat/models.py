from django.db import models

# Create your models here.
class electronics(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=300)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='shop/images', default="")
    
    def __str__(self):
        return self.product_name

class cloths(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=300)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='shop/images', default="")
    def __str__(self):
        return self.product_name

class furnitures(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=300)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='shop/images', default="")
    
    def __str__(self):
        return self.product_name

class vehical(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=300)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='shop/images', default="")
    
    def __str__(self):
        return self.product_name
class camera(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=300)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='shop/images', default="")
    
    def __str__(self):
        return self.product_name