from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'peliculas/home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('peliculas:login')
    else:
        form = UserCreationForm()
    return render(request, 'peliculas/signup.html', {'form': form})