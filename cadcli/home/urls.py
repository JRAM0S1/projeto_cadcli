from django.contrib import admin
from django.urls import path, include
from.import views

urlpatterns = [
    path('', views.home, name='home'),
    path('consultar/', views.consultar, name='consultar'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('salvar/', views.salvar, name='salvar'),
    path('excluir/<int:id>', views.excluir, name='excluir'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('atualizar/<int:id>', views.atualizar, name='atualizar'),
    path('buscar/', views.buscar, name='buscar'),
    path('busca/', views.busca, name='busca')
]