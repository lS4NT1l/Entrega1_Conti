from django.urls import path
from Libreria import views

urlpatterns = [
    path('lector/', views.lector,name='Lectores'),
    path('prestamo/', views.prestamo, name= 'Prestamos'),
    path('libro/', views.libro, name= 'Libros'),
    path('', views.inicio, name= 'Inicio'),
    path('buscarPrestamo/', views.buscarPrestamo, name= 'BuscarPrestamo'),
    path('buscar/', views.buscar)
]