def site_context(request):
    """Disponibiliza variáveis globais para todos os templates."""
    return {
        "site_nome": "Dominando Python",
        "site_descricao": "Aprenda Python com projetos reais",
    }
