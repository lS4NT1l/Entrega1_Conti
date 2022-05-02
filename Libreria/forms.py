from django import forms

class LectorFormulario(forms.Form):
    
    nombre= forms.CharField()
    apellido= forms.CharField()
    telefono= forms.IntegerField()
    libroEnPrestamo= forms.BooleanField(required= False)

class PrestamoFormulario(forms.Form):
    
    lector= forms.CharField()
    libro= forms.CharField()
    fechaDePrestamo= forms.DateField()
    devuelto= forms.BooleanField(required= False)

class LibroFormulario(forms.Form):
    
    nombre= forms.CharField()
    enPrestamo= forms.BooleanField(required= False)
