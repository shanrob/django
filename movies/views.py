from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

def movies(request):
  data = Movie.objects.all()
  print(data)
  return render(request, 'movies/movies.html', {'movies': data})

def home(request):
    return HttpResponse('Home')

def details(request, id):
  data = Movie.objects.get(pk=id)
  return render(request, 'movies/details.html', {'movie': data})

def add(request):
  title = request.POST.get("title")
  year = request.POST.get("year")

  if title and year:
    movie = Movie(title=title, year=year)
    movie.save()
    return HttpResponseRedirect('/movies')

  return render(request, 'movies/add.html')

def delete(request, id):
  movie = Movie.objects.get(pk=id).delete()
  return HttpResponseRedirect('/movies')