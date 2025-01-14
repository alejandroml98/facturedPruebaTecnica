#Librerias
from rest_framework.response import Response # type: ignore
from rest_framework.views import APIView # type: ignore
from rest_framework import status

from . import tableros_collection_querys, tareas_collection_querys


class EstadoTareas(APIView):
    def get(self, request):
        total_tareas = tareas_collection_querys.count_all()
        total_completadas = tareas_collection_querys.count_tarea_by_estado_and_tablero("completada", None)
        total_en_progreso = tareas_collection_querys.count_tarea_by_estado_and_tablero("en progreso", None)
        total_pendientes = tareas_collection_querys.count_tarea_by_estado_and_tablero("pendiente", None)
        respuesta = {
            "status": "ok",
            "total_tareas": total_tareas,
            "tareas_completadas": total_completadas,
            "porcentaje_completadas": total_completadas/total_tareas,
            "tareas_en_progreso": total_en_progreso,
            "porcentaje_en_progreso": total_en_progreso/total_tareas,
            "tareas_pendientes": total_pendientes,
            "porcentaje_pendientes": total_pendientes/total_tareas,
        }
        return Response(respuesta, status.HTTP_200_OK)
    

class EstadoTareasTablero(APIView):
    def get(self, request, pk):
        total_tareas = tareas_collection_querys.count_all(pk)
        total_completadas = tareas_collection_querys.count_tarea_by_estado_and_tablero("completada", pk)
        total_en_progreso = tareas_collection_querys.count_tarea_by_estado_and_tablero("en progreso", pk)
        total_pendientes = tareas_collection_querys.count_tarea_by_estado_and_tablero("pendiente", pk)
        respuesta = {
            "status": "ok",
            "id_tablero": pk,
            "total_tareas": total_tareas,
            "tareas_completadas": total_completadas,
            "porcentaje_completadas": total_completadas/total_tareas,
            "tareas_en_progreso": total_en_progreso,
            "porcentaje_en_progreso": total_en_progreso/total_tareas,
            "tareas_pendientes": total_pendientes,
            "porcentaje_pendientes": total_pendientes/total_tareas,
        }
        return Response(respuesta, status.HTTP_200_OK)