from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from tutoriais.models import Tutorial, Tag
from .models import AssinanteNewsletter


def home(request):
    tutoriais_destaque = Tutorial.objects.filter(publicado=True, destaque=True).prefetch_related("tags")[:6]
    tutoriais_recentes = Tutorial.objects.filter(publicado=True).prefetch_related("tags")[:4]
    tags = Tag.objects.all()[:12]
    context = {
        "tutoriais_destaque": tutoriais_destaque,
        "tutoriais_recentes": tutoriais_recentes,
        "tags": tags,
    }
    return render(request, "core/home.html", context)


def sobre(request):
    return render(request, "core/sobre.html")


@require_POST
def assinar_newsletter(request):
    email = request.POST.get("email", "").strip()
    if email:
        _, criado = AssinanteNewsletter.objects.get_or_create(email=email)
        if criado:
            messages.success(request, "Ótimo! Você está na lista. 🐍")
        else:
            messages.info(request, "Esse email já está cadastrado!")
    return redirect(request.META.get("HTTP_REFERER", "/"))


def handler404(request, exception):
    return render(request, "404.html", status=404)


def handler500(request):
    return render(request, "500.html", status=500)
