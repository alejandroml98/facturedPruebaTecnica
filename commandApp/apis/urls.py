from django.urls import path

from . import tableros_views, tareas_views, seeder_views

urlpatterns = [
    #path("", views.index, name="index"),
    #URL tableros
    path("tablero", tableros_views.TablerosCreate.as_view(), name="tableros_create"),
    path("tablero/<int:pk>", tableros_views.TablerosModify.as_view(), name='tableros_modify'),

    #URL Tareas
    path("tarea", tareas_views.TareasCreate.as_view(), name="tareas_create"),
    path("tarea/<int:pk>", tareas_views.TareasModify.as_view(), name='tareas_modify'),

    #URL seeder
    path("seeder", seeder_views.SeederView.as_view(), name="seeder"),
]