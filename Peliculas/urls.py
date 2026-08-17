from django.urls import path
from Peliculas import views

app_name = 'Peliculas'

urlpatterns = [
    path('', views.home, name='home'),
]
