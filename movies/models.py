# Let's describe some data!

# In Django, you're never writing to SQL directly, you're always writing 
# to Django's ORM (Object-Relational Mapping). The ORM is a layer of abstraction 
# that allows you to interact with your database using Python objects. Django will 
# then translate these objects into SQL queries for you.

from django.db import models

# This is a class that inherits from Django's Model class.
class Movie(models.Model):
  title = models.CharField(max_length=100)
  year = models.IntegerField()

# Now we tell Django we changed our model by running the following command in the terminal:
# python manage.py makemigrations [app name in this case, movies]