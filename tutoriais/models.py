from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings


class Tag(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    cor = models.CharField(max_length=7, default="#1E4D2B", help_text="Cor hex, ex: #1E4D2B")

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ["nome"]

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)


class Tutorial(models.Model):
    NIVEL_CHOICES = [
        ("iniciante", "Iniciante"),
        ("intermediario", "Intermediário"),
        ("avancado", "Avançado"),
    ]

    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=220, blank=True)
    resumo = models.TextField(max_length=300, help_text="Aparece na listagem e no SEO")
    conteudo = models.TextField(help_text="Suporte a Markdown/HTML")
    imagem_capa = models.ImageField(upload_to="tutoriais/capas/", blank=True, null=True)

    nivel = models.CharField(max_length=15, choices=NIVEL_CHOICES, default="iniciante")
    tags = models.ManyToManyField(Tag, blank=True, related_name="tutoriais")
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="tutoriais_escritos",
    )

    publicado = models.BooleanField(default=False)
    destaque = models.BooleanField(default=False, help_text="Aparecer na homepage")
    tempo_leitura = models.PositiveIntegerField(default=5, help_text="Estimativa em minutos")

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    publicado_em = models.DateTimeField(null=True, blank=True)

    visualizacoes = models.PositiveIntegerField(default=0, editable=False)

    class Meta:
        verbose_name = "Tutorial"
        verbose_name_plural = "Tutoriais"
        ordering = ["-publicado_em"]

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("tutoriais:detalhe", kwargs={"slug": self.slug})

    def incrementar_visualizacoes(self):
        Tutorial.objects.filter(pk=self.pk).update(visualizacoes=models.F("visualizacoes") + 1)


class Leitura(models.Model):
    """Rastreia quais tutoriais cada usuário leu."""
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="leituras",
    )
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE, related_name="leituras")
    concluido = models.BooleanField(default=False)
    lido_em = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ["usuario", "tutorial"]
        verbose_name = "Leitura"
        verbose_name_plural = "Leituras"

    def __str__(self):
        return f"{self.usuario.email} → {self.tutorial.titulo}"
