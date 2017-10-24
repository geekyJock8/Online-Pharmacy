from django.conf.urls import url,include
from . import views


urlpatterns = [
        url(r'^$',views.showDashboard2,name='showDashboard2'),
        url(r'^inventory',include('inventory.urls'))
        ]


