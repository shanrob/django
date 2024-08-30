from django.http import HttpResponse
from django.shortcuts import render

def movies(request):
    return render(request, 'movies/movies.html', {'movies': ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight']})

def home(request):
    return HttpResponse('Home')