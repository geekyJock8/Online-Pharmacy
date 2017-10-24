from django.http import HttpResponse

def showDashboard(request):
    return HttpResponse('<h1>This is the Dashboard page of the required user.</h1>')