from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ["email", "nome_exibicao", "nivel", "total_tutoriais_lidos", "is_staff", "criado_em"]
    list_filter = ["nivel", "is_staff", "is_active", "newsletter"]
    search_fields = ["email", "first_name", "last_name"]
    ordering = ["-criado_em"]

    fieldsets = UserAdmin.fieldsets + (
        ("Perfil", {"fields": ("bio", "avatar", "nivel", "github_url", "linkedin_url", "newsletter")}),
    )
