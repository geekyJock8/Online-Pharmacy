from django.http import HttpResponse

def homepage(request):
    return HttpResponse('<h1>This is the homepage of our website. </h1>')