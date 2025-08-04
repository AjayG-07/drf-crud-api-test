from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    name=models.CharField(max_length=50)


class ProductModel(models.Model):
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    descriptions=models.TextField()
    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,related_name='products')