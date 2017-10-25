from django.http import HttpResponse

def showInventory(request):
    return HttpResponse('<h1> This is the Inventory page of the required pharmacy. </h1>')