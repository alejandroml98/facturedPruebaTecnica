from django.urls import path

from . import tareas_views, tableros_views, reportes_views

urlpatterns = [
    #path("", views.index, name="index"),
    #URL tableros
    path("tablero", tableros_views.TablerosList.as_view(), name="tableros_list"),
    path("tablero/<int:pk>", tableros_views.TablerosGet.as_view(), name='tableros_get'),

    #URL Tareas
    path("tarea", tareas_views.TareasList.as_view(), name="tareas_list"),
    path("tarea/<int:pk>", tareas_views.TareasGet.as_view(), name='tareas_get'),
    

    #URL reportes
    path("reportes/tareas", reportes_views.EstadoTareas.as_view(), name="reporte_tareas"),
    path("reportes/tareas/<int:pk>", reportes_views.EstadoTareasTablero.as_view(), name="reporte_tareas_tablero"),
]