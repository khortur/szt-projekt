from django.db import models
from django.utils import timezone


class Item(models.Model):
    brand = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField(default=0)
    image = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.name

class Purchase(models.Model):
    item = models.ForeignKey('store.Item', related_name='purchases')
    buyer = models.ForeignKey('auth.User')
    amount = models.IntegerField(default=0, null=True)

    def total_price(self):
        return self.amount * self.item.price

    def __str__(self):
        return self.item.name + " : " + self.buyer.username + " : " + self.amount.__str__()