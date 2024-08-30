from .models import Movie
from django.contrib import admin

# Register your models here.
# This is where we tell our app to make the Movie model visible on the admin page.

admin.site.register(Movie)