from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Usuário customizado com campos extras para o perfil de aprendizado."""
    bio = models.TextField(blank=True, max_length=500)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    nivel = models.CharField(
        max_length=20,
        choices=[
            ("iniciante", "Iniciante"),
            ("intermediario", "Intermediário"),
            ("avancado", "Avançado"),
        ],
        default="iniciante",
    )
    newsletter = models.BooleanField(default=True, help_text="Receber newsletter semanal")
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.email

    @property
    def nome_exibicao(self):
        return self.get_full_name() or self.email.split("@")[0]

    @property
    def total_tutoriais_lidos(self):
        return self.leituras.filter(concluido=True).count()
