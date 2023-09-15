from django.db import models

# Create your models here.

class Customer(models.Model):
    cust_name = models.CharField(max_length=254)

    def __str__(self):
        return self.cust_name
