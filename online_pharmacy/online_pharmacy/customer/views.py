from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.apps import apps
from .models import customer


def showDashboard1(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        member = apps.get_model('customer.customer')
        try:
             user = customer.objects.get(username=username)
             return HttpResponse('<h1>This is the Dashboard page of thknnke required user.</h1>')
        except:
            return HttpResponse('<h1>Sorry.</h1>')
    return HttpResponse('<h1>This is the Dashboard page of thknnke required user.</h1>')