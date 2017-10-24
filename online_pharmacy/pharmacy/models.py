from django.db import models

class pharmacy(models.Model):
    pharmacy_id = models.CharField(max_length=20,primary_key=True)
    pharmacy_name = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    owner_fname = models.CharField(max_length=50)
    owner_lname = models.CharField(max_length=50)
    vat_no = models.ImageField()
    drug_license = models.ImageField()
    address_street = models.TextField()
    address_city = models.CharField(max_length=20)
    address_state = models.CharField(max_length=20)
    address_pincode = models.IntegerField()

class contact_pharmacy(models.Model):
    pharmacy = models.ForeignKey(pharmacy,on_delete=models.CASCADE)
    contact_no = models.IntegerField()


class pharmacy_notifications(models.Model):
    pharmacy_id = models.ForeignKey(pharmacy,on_delete=models.CASCADE)
    time_of_arrival = models.DateTimeField(auto_now_add=True,blank=True)
    content = models.TextField()