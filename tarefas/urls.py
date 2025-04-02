from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.listaTarefa, name='lista-tarefa'),
    path('tarefa/<int:id>', views.tarefaView, name='tarefa-view'),
     path('novatarefa/', views.novaTarefa, name='nova-tarefa'),
]
