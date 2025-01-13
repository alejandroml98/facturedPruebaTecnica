#Librerias
from rest_framework.response import Response # type: ignore
from rest_framework.views import APIView # type: ignore
from rest_framework import status

from .mongo_connection import prueba


class TareasList(APIView):
    def get(self, request):
        datos = prueba()
        respuesta = {
            "status": "ok", 
            "description":"Tarea creada correctamente", 
            "data": datos.to_list()
        }
        return Response(respuesta, status.HTTP_200_OK)