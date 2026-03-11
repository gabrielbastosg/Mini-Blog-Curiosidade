from collections import Counter
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Curiosidade
from django.utils.text import slugify
import re


# Função auxiliar para destacar termos
def destacar_texto(texto, termo):
    if not termo:
        return texto

    regex = re.compile(re.escape(termo), re.IGNORECASE)

    return regex.sub(r'<span class="destaque">\g<0></span>', texto)


def index(request):

    termo = request.GET.get('q', '')
    categoria = request.GET.get('categoria', '')
    ordenacao = request.GET.get('ordenacao', 'data_desc')

    curiosidades = Curiosidade.objects.all()

    # filtro por título
    if termo:
        curiosidades = curiosidades.filter(titulo__icontains=termo)

    # filtro por categoria
    if categoria:
        curiosidades = curiosidades.filter(categoria=categoria)

    # ordenação
    if ordenacao == 'data_asc':
        curiosidades = curiosidades.order_by('data_criacao')

    elif ordenacao == 'titulo_asc':
        curiosidades = curiosidades.order_by('titulo')

    elif ordenacao == 'titulo_desc':
        curiosidades = curiosidades.order_by('-titulo')

    else:
        curiosidades = curiosidades.order_by('-data_criacao')

    # criar slug e destaque
    curiosidades_destacadas = []

    for c in curiosidades:
        c.slug_categoria = slugify(c.categoria)
        c.titulo_destaque = destacar_texto(c.titulo, termo)
        c.conteudo_destaque = destacar_texto(c.conteudo, termo)
        curiosidades_destacadas.append(c)

    # PAGINAÇÃO
    paginator = Paginator(curiosidades_destacadas, 6)  # 6 curiosidades por página
    page = request.GET.get('page')
    curiosidades_paginadas = paginator.get_page(page)

    # categorias únicas
    categorias = Curiosidade.objects.values_list('categoria', flat=True).distinct()

    # contagem por categoria
    todas_curiosidades = Curiosidade.objects.all()
    contagem_categorias = Counter([c.categoria for c in todas_curiosidades])

    categorias_com_contagem = [
        (cat, contagem_categorias[cat]) for cat in categorias
    ]

    total_curiosidades = todas_curiosidades.count()

    return render(request, 'curiosidades/index.html', {

        'curiosidades': curiosidades_paginadas,
        'termo': termo,
        'categorias_com_contagem': categorias_com_contagem,
        'categoria_selecionada': categoria,
        'ordenacao': ordenacao,
        'total_curiosidades': total_curiosidades,

    })


def detalhe(request, curiosidade_id):

    curiosidade = get_object_or_404(Curiosidade, pk=curiosidade_id)

    curiosidade.slug_categoria = slugify(curiosidade.categoria)

    # destacar termo se vier da busca
    termo = request.GET.get('q', '')

    curiosidade.titulo_destaque = destacar_texto(curiosidade.titulo, termo)
    curiosidade.conteudo_destaque = destacar_texto(curiosidade.conteudo, termo)

    return render(
        request,
        'curiosidades/detalhe.html',
        {'curiosidade': curiosidade}
    )