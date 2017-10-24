from django.http import HttpResponse
from django.apps import apps
from .models import pharmacy

def showDashboard2(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        member = apps.get_model('pharmacy.pharmacy')
        try:
             user = pharmacy.objects.get(pharmacy_name=username)
             return HttpResponse('<h1>This is the Dashboard page of thknnke required pharmacy.</h1>')
        except:
            return HttpResponse('<h1>Sorry.</h1>')
    else:
        return HttpResponse('<h1>This is the Dashboard page of thknnke required pharmacy.</h1>')
