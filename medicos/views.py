from django.shortcuts import render, get_object_or_404
from .models import Medico

def lista_medicos(request):
    # Filtros da URL
    search = request.GET.get('search', '')
    specialty = request.GET.get('specialty', '')
    sort = request.GET.get('sort', '')

    # Filtra os médicos, carrega apenas campos essenciais para poupar desempenho
    medicos = Medico.objects.only('id', 'nome', 'especialidade', 'preco', 'tempo_consulta', 'foto_perfil','views')

    if search:
        medicos = medicos.filter(nome__icontains=search)

    if specialty and specialty != 'all':
        medicos = medicos.filter(especialidade=specialty)

    if sort == 'preco_asc':
        medicos = medicos.order_by('preco')
    elif sort == 'preco_desc':
        medicos = medicos.order_by('-preco')
    elif sort == 'views_desc':
        medicos = medicos.order_by('views')


    # Obtendo as especialidades distintas
    especialidades = Medico.objects.values_list('especialidade', flat=True).distinct()

    return render(request, 'medicos/lista_medicos.html', {
        'medicos': medicos,
        'especialidades': especialidades,
        'search': search,
        'specialty': specialty,
    })


def perfil_medico(request, id):
    # Todos os detalhes do medico
    medico = get_object_or_404(Medico.objects.prefetch_related('formacoes'), id=id)
    return render(request, 'medicos/perfil_medico.html', {'medico': medico})

