from django.urls import path
from . import views

app_name = "tutoriais"

urlpatterns = [
    path("", views.lista, name="lista"),
    path("<slug:slug>/", views.detalhe, name="detalhe"),
    path("<slug:slug>/concluir/", views.marcar_concluido, name="marcar_concluido"),
]
