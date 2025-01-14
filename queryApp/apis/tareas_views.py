#Librerias
from rest_framework.response import Response # type: ignore
from rest_framework.views import APIView # type: ignore
from rest_framework import status

from . import tareas_collection_querys


class TareasList(APIView):
    def get(self, request):
        page_size = int(request.GET.get("page_size",10))
        page = int(request.GET.get("page",1))
        skip = (page-1)*page_size
        datos = tareas_collection_querys.list_all_tareas(skip, page_size)
        tareas_count = tareas_collection_querys.count_all()
        respuesta = {
            "status": "ok",
            "page": page,
            "page_size": page_size,
            "total_pages": (tareas_count + page_size - 1) // page_size,
            "total": tareas_count,
            "data": list(datos)
        }
        return Response(respuesta, status.HTTP_200_OK)
    

class TareasGet(APIView):
    def get(self, request, pk):
        datos = tareas_collection_querys.get_tarea(pk)
        respuesta = {
            "status": "ok",
            "data": datos
        }
        return Response(respuesta, status.HTTP_200_OK)