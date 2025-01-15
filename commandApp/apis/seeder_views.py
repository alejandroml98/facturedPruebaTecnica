#Librerias
from rest_framework.response import Response # type: ignore
from rest_framework.views import APIView # type: ignore
from rest_framework import status

#seeder
from .seeder import seed


class SeederView(APIView):
    def post(self, request):
        cantidad_tableros = int(request.data.get("cantidad_tableros",0))
        cantidad_tareas = int(request.data.get("cantidad_tareas",0))

        if 0 in [cantidad_tableros, cantidad_tareas]:
            return Response({"status": "error", "description":"campos [cantidad_tableros, cantidad_tareas] son obligatorios"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            seed(cantidad_tableros, cantidad_tareas)
            return Response({"status": "ok", "description":"seeder completado"}, status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({"status": "error", "description":"seeder no se completo"}, status=status.HTTP_400_BAD_REQUEST)
            
        