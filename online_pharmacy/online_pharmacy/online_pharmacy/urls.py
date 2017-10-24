from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'',include('Register_and_login.urls')),
    url(r'^homepage/',include('MainPage.urls')),
    url(r'^username/cart/',include('cart.urls')),
    url(r'^username/',include('customer.urls')),
    url(r'^pharmacy_name/',include('pharmacy.urls')),
    url(r'^pharmacy_name/inventory',include('inventory.urls')),
    url(r'^search/all_search=pcm',include('items.urls')),
    url(r'^$', include('order.urls')),
    url(r'^admin/', admin.site.urls)
]
