from django.conf.urls import url,include
from . import views


urlpatterns = [
    url(r'show/',views.showInventory,name="showInventory"),
    url(r'create/',views.createInventory,name="createInventory"),
    ]
