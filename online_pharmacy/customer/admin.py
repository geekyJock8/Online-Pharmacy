from django.contrib import admin

from .models import customer,address_list,contact_customer,customer_notifications

admin.site.register(customer)
admin.site.register(address_list)
admin.site.register(contact_customer)
admin.site.register(customer_notifications)

