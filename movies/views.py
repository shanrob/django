from django.http import HttpResponse

def movies(request):
    return HttpResponse('Movies')

def home(request):
    return HttpResponse('Home')