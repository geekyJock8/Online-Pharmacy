from django.http import HttpResponse

def orderPlaced(request):
    return HttpResponse('<h1> Your order with <order id> is placed. </h1>')

def addressPage(request):
    return HttpResponse('<h1> Page asking for address for delievery. </h1>')

def choicePage(request):
    return HttpResponse('<h1> Choices are given on this page </h1> ')

def prescriptionPage(request):
    return HttpResponse('<h1> Page for uploading prescription </h1>')
