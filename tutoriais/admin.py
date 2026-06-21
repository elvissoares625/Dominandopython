from django.contrib import admin
from django.utils import timezone
from .models import Tutorial, Tag, Leitura


@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ["titulo", "nivel", "autor", "publicado", "destaque", "visualizacoes", "publicado_em"]
    list_filter = ["publicado", "destaque", "nivel", "tags"]
    search_fields = ["titulo", "resumo"]
    prepopulated_fields = {"slug": ("titulo",)}
    filter_horizontal = ["tags"]
    date_hierarchy = "criado_em"
    actions = ["publicar", "despublicar"]

    def publicar(self, request, queryset):
        queryset.update(publicado=True, publicado_em=timezone.now())
        self.message_user(request, f"{queryset.count()} tutoriais publicados.")
    publicar.short_description = "Publicar tutoriais selecionados"

    def despublicar(self, request, queryset):
        queryset.update(publicado=False)
        self.message_user(request, f"{queryset.count()} tutoriais despublicados.")
    despublicar.short_description = "Despublicar tutoriais selecionados"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["nome", "slug", "cor"]
    prepopulated_fields = {"slug": ("nome",)}


@admin.register(Leitura)
class LeituraAdmin(admin.ModelAdmin):
    list_display = ["usuario", "tutorial", "concluido", "lido_em"]
    list_filter = ["concluido"]
    raw_id_fields = ["usuario", "tutorial"]
