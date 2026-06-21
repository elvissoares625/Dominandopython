# dominandopython.com

Site de referência para aprender Python com projetos reais, construído com Django.

## Setup local

```bash
git clone https://github.com/seu-usuario/dominandopython
cd dominandopython

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt

cp .env.example .env
# edite o .env com suas configurações

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse: http://localhost:8000  
Admin: http://localhost:8000/admin

## Estrutura

```
config/          → Configurações Django (settings, urls, wsgi)
core/            → Homepage, newsletter, páginas estáticas
tutoriais/       → CRUD de tutoriais, tags, leituras
accounts/        → CustomUser, perfil, progresso
templates/       → Todos os templates HTML
static/          → CSS, JS, imagens
```

## Fluxo de publicação de tutorial

1. Acesse /admin → Tutoriais → Adicionar tutorial
2. Preencha título, resumo, conteúdo (suporte a HTML)
3. Adicione tags e defina o nível
4. Marque "Publicado" e salve
5. Opcionalmente marque "Destaque" para aparecer na homepage

## Variáveis de ambiente (.env)

| Variável | Descrição |
|---|---|
| `SECRET_KEY` | Chave secreta Django |
| `DEBUG` | `True` em dev, `False` em prod |
| `ALLOWED_HOSTS` | Hosts permitidos |
| `DATABASE_URL` | URL do banco (PostgreSQL em prod) |
| `EMAIL_BACKEND` | Backend de email |
