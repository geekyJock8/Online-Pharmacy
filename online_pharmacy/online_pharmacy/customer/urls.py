from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.showDashboard1,name='showDashboard1'),
    ]


