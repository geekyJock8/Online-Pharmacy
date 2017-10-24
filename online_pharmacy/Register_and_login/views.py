from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>This is the page giving u the choice of registration and login.</h1>')

def user_registration(request):
    return HttpResponse('<h1>This is registration page for user.</h1>')

def pharmacy_registration(request):
    return HttpResponse('<h1>This is registration page for Pharmacy.</h1>')

def user_login(request):
    return HttpResponse('<h1>This is login page for user.</h1>')

def pharmacy_login(request):
    return HttpResponse('<h1>This is login page for pharmacy.</h1>')

