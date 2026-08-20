from django.contrib.auth import views as auth_views
from django.urls import path
from Peliculas import views

app_name = 'Peliculas'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='peliculas/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')

]
