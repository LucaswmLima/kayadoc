from django.shortcuts import render, get_object_or_404
from .models import Medico

def lista_medicos(request):
    # Pegando os filtros da URL
    search = request.GET.get('search', '')
    specialty = request.GET.get('specialty', '')
    sort = request.GET.get('sort', '')  # Usando o parâmetro 'sort' para a ordenação

    # Filtrando os médicos
    medicos = Medico.objects.all()

    if search:
        medicos = medicos.filter(nome__icontains=search)

    if specialty and specialty != 'all':
        medicos = medicos.filter(especialidade=specialty)

    # Ordenação por preço
    if sort == 'preco_asc':
        medicos = medicos.order_by('preco')
    elif sort == 'preco_desc':
        medicos = medicos.order_by('-preco')

    # Obtendo as especialidades de forma distinta
    especialidades = Medico.objects.values_list('especialidade', flat=True).distinct()

    return render(request, 'medicos/lista_medicos.html', {
        'medicos': medicos,
        'especialidades': especialidades,
        'search': search,
        'specialty': specialty,
    })


def perfil_medico(request, id):
    medico = get_object_or_404(Medico, id=id)
    return render(request, 'medicos/perfil_medico.html', {'medico': medico})
