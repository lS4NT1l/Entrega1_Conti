from django.http import HttpResponse
from django.shortcuts import render
from Libreria.forms import LectorFormulario, PrestamoFormulario, LibroFormulario
from Libreria.models import Lector, Prestamo, Libro


def lector(request):
    
    if request.method == 'POST':

        miFormulario= LectorFormulario(request.POST)

        if miFormulario.is_valid():
            
            info= miFormulario.cleaned_data

            lector= Lector(nombre= info['nombre'], apellido= info['apellido'], telefono= info['telefono'], libroEnPrestamo= info['libroEnPrestamo'])

            lector.save()

            return render(request, 'Libreria/inicio.html')

    else:

        miFormulario= LectorFormulario()    


    return render(request,'Libreria/lector.html', {'miFormulario':miFormulario})

def prestamo(request):
    
    if request.method == 'POST':

        miFormulario= PrestamoFormulario(request.POST)

        if miFormulario.is_valid():
            
            info= miFormulario.cleaned_data

            prestamo= Prestamo(lector= info['lector'], libro= info['libro'], fechaDePrestamo= info['fechaDePrestamo'], devuelto= info['devuelto'])

            prestamo.save()

            return render(request, 'Libreria/inicio.html')

    else:

        miFormulario= PrestamoFormulario()    


    return render(request,'Libreria/prestamo.html', {'miFormulario':miFormulario})

def libro(request):

    if request.method == 'POST':

        miFormulario= LibroFormulario(request.POST)

        if miFormulario.is_valid():
            
            info= miFormulario.cleaned_data

            libro= Libro(nombre= info['nombre'], enPrestamo= info['enPrestamo'])

            libro.save()

            return render(request, 'Libreria/inicio.html')

    else:

        miFormulario= LibroFormulario()
    

    return render(request,'Libreria/libro.html', {'miFormulario':miFormulario})


def inicio(request):
    

    return render(request,'Libreria/inicio.html')

def buscarPrestamo(request):



    return render(request, 'Libreria/buscarPrestamo.html')

def buscar(request):
    if request.GET["lector"]:
       

        lector= request.GET["lector"]
        prestamos= Prestamo.objects.filter(lector__icontains=lector)

        return render(request, 'Libreria/resultadosBusqueda.html', {"prestamos":prestamos, "lector":lector})
    else:

        respuesta= "No ingresaste datos" 

    return HttpResponse(respuesta)
  



