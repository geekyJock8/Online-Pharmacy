from django.db import models
from customer import models as customer_models
from pharmacy import models as pharmacy_models


class order(models.Model):
    pharmacy_id = models.ForeignKey(pharmacy_models.pharmacy)
    buyer = models.ForeignKey(customer_models.customer)
    order_id = models.CharField(max_length=20,primary_key=True)
    order_date = models.DateField()
    prescription = models.ImageField()
    address_street = models.TextField()
    address_city = models.CharField(max_length=20)
    address_state = models.CharField(max_length=20)
    address_pincode = models.IntegerField()
    delivered_date=models.DateField()


