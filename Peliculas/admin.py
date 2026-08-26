from django.contrib import admin

from .models import Pelicula


@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'anio_estreno', 'creado_por', 'fecha_creacion')
    list_filter = ('genero', 'disponible')
    search_fields = ('titulo',)
