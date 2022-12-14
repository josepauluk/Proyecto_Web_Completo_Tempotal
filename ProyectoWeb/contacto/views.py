from django.shortcuts import render
from .forms import FormularioContacto

# Create your views here.

def contacto(request):

    Formulario_Contacto=FormularioContacto()
    return render(request, 'contacto/contacto.html', {'miFormulario': Formulario_Contacto})