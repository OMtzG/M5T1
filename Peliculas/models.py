from django.conf import settings
from django.db import models


class Pelicula(models.Model):
    class Genero(models.TextChoices):
        ACCION = 'ACCION', 'Acción'
        COMEDIA = 'COMEDIA', 'Comedia'
        DRAMA = 'DRAMA', 'Drama'
        TERROR = 'TERROR', 'Terror'
        CIENCIA_FICCION = 'CIENCIA_FICCION', 'Ciencia ficción'
        ANIMACION = 'ANIMACION', 'Animación'
        OTRO = 'OTRO', 'Otro'

    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=20, choices=Genero.choices, default=Genero.OTRO)
    anio_estreno = models.PositiveIntegerField()
    duracion_minutos = models.PositiveIntegerField()
    sinopsis = models.TextField(blank=True)
    calificacion = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    disponible = models.BooleanField(default=True)
    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='peliculas'
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.titulo
