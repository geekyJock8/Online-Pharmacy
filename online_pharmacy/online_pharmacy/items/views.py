from django.http import HttpResponse

def showSearch(request):
    return HttpResponse('<h1> This is the search page after searching of the element </h1>')
