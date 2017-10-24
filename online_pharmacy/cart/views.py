from django.http import HttpResponse

def showCart(request):
    return HttpResponse('<h1>This is the cart of the required user. </h1>')

