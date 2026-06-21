from django.db import models


class AssinanteNewsletter(models.Model):
    """Visitantes que assinaram a newsletter sem criar conta."""
    email = models.EmailField(unique=True)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Assinante Newsletter"
        verbose_name_plural = "Assinantes Newsletter"
        ordering = ["-criado_em"]

    def __str__(self):
        return self.email
