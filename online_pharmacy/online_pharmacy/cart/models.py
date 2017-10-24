from django.db import models
from django.apps import apps



class contains(models.Model):
    cart_id = models.ForeignKey('customer.customer',primary_key=True,on_delete=models.CASCADE),
    item_id = models.ForeignKey('items.item',primary_key=True,on_delete=models.CASCADE),
    quantity = models.IntegerField(default=0)

