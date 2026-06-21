from django.contrib import admin
from .models import AssinanteNewsletter


@admin.register(AssinanteNewsletter)
class AssinanteNewsletterAdmin(admin.ModelAdmin):
    list_display = ["email", "ativo", "criado_em"]
    list_filter = ["ativo"]
    search_fields = ["email"]
