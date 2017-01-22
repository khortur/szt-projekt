from django.db import models
from django.utils import timezone


class Item(models.Model):
    brand = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name