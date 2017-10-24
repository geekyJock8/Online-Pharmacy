from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import csrf
from django.views import View
from django.apps import apps

#from online_pharmacy.customer.models import customer
#from online_pharmacy import customer

#from customer.models import customer
def index(request):
    return HttpResponse('<h1>This is the page giving u the choice of registration and login.</h1>')

def user_registration(request):
    return render(request,'Register_and_login/register.html',{})

def pharmacy_registration(request):
    return render(request, 'Register_and_login/register_pharmacy.html', {})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('passsword', False)
        fname = request.POST.get('lname', False)
        lname = request.POST.get('fname', False)
        age = request.POST.get('age', False)
        email = request.POST.get('email', False)
        cart_id = request.POST.get('cart_id', False)
        member=apps.get_model('customer.customer')
        a =member(username,password, fname,lname,age,email, cart_id)
        if a is not None:
             a.save()

    return render(request,'Register_and_login/login.html',{})


def pharmacy_login(request):
    if request.method == 'POST':
        pharmacy_id= request.POST.get('pharmacy_id', False)
        pharmacy_name = request.POST.get('pharmacy_name', False)
        password = request.POST.get('passsword', False)
        owner_fname= request.POST.get('fname', False)
        owner_lname= request.POST.get('lname', False)
        vat_no = request.POST.get('vat', False)
        drug = request.POST.get('drug', False)
        street = request.POST.get('street', False)
        city = request.POST.get('city', False)
        state = request.POST.get('state', False)
        pincode = request.POST.get('pincode', False)
        member=apps.get_model('pharmacy.pharmacy')
        b = member(pharmacy_id,pharmacy_name,password,owner_fname,owner_lname,vat_no,drug, street,city,state,pincode)
        if b is not None:
             b.save()
    return render(request, 'Register_and_login/login_pharmacy.html', {})

