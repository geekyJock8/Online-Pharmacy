from django.db import models
from customer import models as customer_models
from items import models as item_models


class contains(models.Model):
    cart_id = models.ForeignKey(customer_models.customer,primary_key=True,on_delete=models.CASCADE),
    item_id = models.ForeignKey(item_models.item,primary_key=True,on_delete=models.CASCADE),
    quantity = models.IntegerField(default=0)

