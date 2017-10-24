from django.contrib import admin

from .models import pharmacy,contact_pharmacy,pharmacy_notifications

admin.site.register(pharmacy)
admin.site.register(contact_pharmacy)
admin.site.register(pharmacy_notifications)


