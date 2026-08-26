# M5T1 — Catálogo de Películas Django

## Entorno virtual
Crear el entorno virtual (una sola vez):
```
python -m venv .venv
```

Activarlo:
- Windows (PowerShell):
```
.venv\Scripts\Activate.ps1
```
- Windows (cmd):
```
.venv\Scripts\activate.bat
```
- Linux/macOS:
```
source .venv/bin/activate
```

Desactivarlo cuando termines:
```
deactivate
```

## Instalación
```
pip install -r requirements.txt
```

## Preparar base de datos
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py createsuperuser
```

## Cargar datos de ejemplo
```
python manage.py loaddata peliculas
```

## Ejecutar
```
python manage.py runserver
```

## URLs principales
- Listado: http://127.0.0.1:8000/peliculas/
- Detalle: http://127.0.0.1:8000/peliculas/<id>/
- Añadir: http://127.0.0.1:8000/peliculas/agregar/ (requiere autenticación)
- Registro: http://127.0.0.1:8000/signup/
- Login: http://127.0.0.1:8000/login/
- Admin: http://127.0.0.1:8000/admin/

## Ejemplos de búsqueda y filtros
- Búsqueda: /peliculas/?q=matrix
- Filtro por género: /peliculas/?genero=CIENCIA_FICCION
- Ordenar: /peliculas/?order=anio&dir=desc
- Combinado: /peliculas/?q=a&genero=COMEDIA&order=calificacion&dir=asc&page=1

## Autor
- Óscar Martinez Galan

## Fecha de creación
2026-06-03
