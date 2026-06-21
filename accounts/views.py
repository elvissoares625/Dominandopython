from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import PerfilForm


@login_required
def perfil(request):
    """Página de perfil do usuário com seu progresso."""
    leituras = request.user.leituras.select_related("tutorial").order_by("-lido_em")[:10]
    context = {
        "leituras_recentes": leituras,
        "total_lidos": request.user.total_tutoriais_lidos,
    }
    return render(request, "accounts/perfil.html", context)


@login_required
def editar_perfil(request):
    if request.method == "POST":
        form = PerfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect("accounts:perfil")
    else:
        form = PerfilForm(instance=request.user)
    return render(request, "accounts/editar_perfil.html", {"form": form})
