from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

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
    return render(request, 'Peliculas/signup.html', {'form': form})