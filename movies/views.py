from django.http import HttpResponse
from django.shortcuts import render

data = {
  'movies': [
    {
      'title': 'The Shawshank Redemption',
      'year': 1994
    },
    {
      'title': 'The Godfather',
      'year': 1972
    },
    {
      'title': 'The Dark Knight',
      'year': 2008
    }
  ]
}

def movies(request):
    return render(request, 'movies/movies.html', {'movies': ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight']})

def home(request):
    return HttpResponse('Home')