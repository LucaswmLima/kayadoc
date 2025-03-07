from django.shortcuts import render, get_object_or_404
from .models import Medico

def lista_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'medicos/lista_medicos.html', {'medicos': medicos})

def perfil_medico(request, id):
    medico = get_object_or_404(Medico, id=id)
    return render(request, 'medicos/perfil_medico.html', {'medico': medico})
