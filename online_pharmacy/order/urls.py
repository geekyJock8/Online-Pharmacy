from django.conf.urls import url,include
from . import views


urlpatterns = [
    url(r'^order/address',views.addressPage,name='addressPage1'),
    url(r'^order_with_prescription/address',views.addressPage,name='addressPage2'),
    url(r'^order_with_prescription/specify',views.choicePage,name='choicePage'),
    url(r'^order_with_prescription/placed',views.orderPlaced,name='orderPlaced1'),
    url(r'^order_with_prescription',views.prescriptionPage,name='prescriptionPage'),
    url(r'^order/placed',views.orderPlaced,name='orderPlaced2')
    ]