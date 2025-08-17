from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_equipamentos, name='listar_equipamentos'),
    path('adicionar/', views.adicionar_equipamento, name='adicionar_equipamento'),
    path('editar/<str:pk>/', views.editar_equipamento, name='editar_equipamento'),
    path('remover/<str:pk>/', views.remover_equipamento, name='remover_equipamento'),
]
