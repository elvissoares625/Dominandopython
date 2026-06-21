from django import forms
from .models import CustomUser


class PerfilForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "bio", "avatar", "nivel", "github_url", "linkedin_url", "newsletter"]
        widgets = {
            "bio": forms.Textarea(attrs={"rows": 4, "placeholder": "Conte um pouco sobre você..."}),
            "github_url": forms.URLInput(attrs={"placeholder": "https://github.com/usuario"}),
            "linkedin_url": forms.URLInput(attrs={"placeholder": "https://linkedin.com/in/usuario"}),
        }
        labels = {
            "first_name": "Nome",
            "last_name": "Sobrenome",
            "bio": "Bio",
            "avatar": "Foto de perfil",
            "nivel": "Seu nível em Python",
            "github_url": "GitHub",
            "linkedin_url": "LinkedIn",
            "newsletter": "Quero receber a newsletter semanal",
        }
