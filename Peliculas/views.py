from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PeliculaForm
from .models import Pelicula

ORDEN_PERMITIDO = {
    'titulo': 'titulo',
    'anio': 'anio_estreno',
    'calificacion': 'calificacion',
}


def home(request):
    return render(request, 'peliculas/home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Peliculas:login')
    else:
        form = UserCreationForm()
    return render(request, 'peliculas/signup.html', {'form': form})


def lista_peliculas(request):
    peliculas = Pelicula.objects.all()

    query = request.GET.get('q', '').strip()
    if query:
        peliculas = peliculas.filter(
            Q(titulo__icontains=query) | Q(sinopsis__icontains=query)
        )

    genero = request.GET.get('genero', '').strip()
    if genero:
        peliculas = peliculas.filter(genero=genero)

    order = request.GET.get('order', '')
    campo_orden = ORDEN_PERMITIDO.get(order)
    direccion = request.GET.get('dir', 'asc')
    if campo_orden:
        if direccion == 'desc':
            campo_orden = f'-{campo_orden}'
        peliculas = peliculas.order_by(campo_orden)

    paginator = Paginator(peliculas, 6)
    page_obj = paginator.get_page(request.GET.get('page'))

    parametros = request.GET.copy()
    parametros.pop('page', None)

    context = {
        'page_obj': page_obj,
        'peliculas': page_obj.object_list,
        'query': query,
        'genero_seleccionado': genero,
        'generos': Pelicula.Genero.choices,
        'order': order,
        'dir': direccion,
        'querystring': parametros.urlencode(),
    }
    return render(request, 'peliculas/lista_peliculas.html', context)


def detalle_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    return render(request, 'peliculas/detalle_pelicula.html', {'pelicula': pelicula})


@login_required
def agregar_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            pelicula = form.save(commit=False)
            pelicula.creado_por = request.user
            pelicula.save()
            return redirect('Peliculas:lista_peliculas')
    else:
        form = PeliculaForm()
    return render(request, 'peliculas/agregar_pelicula.html', {'form': form})


@login_required
def eliminar_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    if request.method == 'POST':
        pelicula.delete()
        return redirect('Peliculas:lista_peliculas')
    return render(request, 'peliculas/eliminar_pelicula.html', {'pelicula': pelicula})
