from django.db import models
from rest_framework import serializers
# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    inventory=models.DecimalField(max_digits=10,decimal_places=2)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.CharField(max_length=255)
     
    def _str_(self):
        return self.name