from django.db import models

# Create your models here.
class Pelicula(models.Model):
   title = models.CharField(max_length=200)
   author = models.CharField(max_length=100)
   published_at = models.DateField()