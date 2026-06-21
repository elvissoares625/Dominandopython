from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q
from .models import Tutorial, Tag, Leitura


def lista(request):
    """Lista paginada de tutoriais com filtros por nível e tag."""
    tutoriais = Tutorial.objects.filter(publicado=True).prefetch_related("tags").select_related("autor")

    nivel = request.GET.get("nivel")
    tag_slug = request.GET.get("tag")
    busca = request.GET.get("q")

    if nivel:
        tutoriais = tutoriais.filter(nivel=nivel)
    if tag_slug:
        tutoriais = tutoriais.filter(tags__slug=tag_slug)
    if busca:
        tutoriais = tutoriais.filter(
            Q(titulo__icontains=busca) | Q(resumo__icontains=busca)
        )

    tags = Tag.objects.all()
    context = {
        "tutoriais": tutoriais,
        "tags": tags,
        "nivel_ativo": nivel,
        "tag_ativa": tag_slug,
        "busca": busca,
    }
    return render(request, "tutoriais/lista.html", context)


def detalhe(request, slug):
    """Página de leitura do tutorial."""
    tutorial = get_object_or_404(Tutorial, slug=slug, publicado=True)
    tutorial.incrementar_visualizacoes()

    ja_leu = False
    if request.user.is_authenticated:
        ja_leu = Leitura.objects.filter(usuario=request.user, tutorial=tutorial, concluido=True).exists()

    relacionados = (
        Tutorial.objects
        .filter(publicado=True, tags__in=tutorial.tags.all())
        .exclude(pk=tutorial.pk)
        .distinct()[:3]
    )

    context = {
        "tutorial": tutorial,
        "relacionados": relacionados,
        "ja_leu": ja_leu,
    }
    return render(request, "tutoriais/detalhe.html", context)


@login_required
def marcar_concluido(request, slug):
    """Endpoint AJAX para marcar tutorial como lido."""
    if request.method != "POST":
        return JsonResponse({"erro": "Método não permitido"}, status=405)

    tutorial = get_object_or_404(Tutorial, slug=slug, publicado=True)
    leitura, criada = Leitura.objects.get_or_create(
        usuario=request.user,
        tutorial=tutorial,
        defaults={"concluido": True},
    )
    if not criada:
        leitura.concluido = not leitura.concluido
        leitura.save(update_fields=["concluido", "lido_em"])

    return JsonResponse({"concluido": leitura.concluido})
