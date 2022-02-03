import email
from unicodedata import name
from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=190, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=190, null=True)
    age = models.CharField(max_length=190, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name
    