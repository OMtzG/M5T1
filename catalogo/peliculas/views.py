from django.shortcuts import render

from catalogo.peliculas.models import Pelicula

# Create your views here.
def latest_peliculas(request):
   peliculas = Pelicula.objects.order_by("-published_at")[:5]
   return render(request, "peliculas.html", {"peliculas": peliculas})