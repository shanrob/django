from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

def movies(request):
  data = Movie.objects.all()
  print(data)
  return render(request, 'movies/movies.html', {'movies': data})

def home(request):
    return HttpResponse('Home')