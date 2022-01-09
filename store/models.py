from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50, default='', unique=True)
    number = models.IntegerField(null=False, unique=True)
    price = models.IntegerField(null=False, unique=True)