from django.db import models
#from pharmacy import models as pharmacy_models
#from items import models as item_models


class sells(models.Model):
    pharmacy_id = models.ForeignKey('pharmacy.pharmacy',on_delete = models.CASCADE)
    item_id = models.ForeignKey('items.item',on_delete = models.CASCADE)
    quantity = models.IntegerField()
    price_per_item = models.FloatField()
