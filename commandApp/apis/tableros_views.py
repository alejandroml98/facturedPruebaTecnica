#Librerias
from rest_framework.response import Response # type: ignore
from rest_framework.views import APIView # type: ignore
from rest_framework import status

#serializers
from .serializer import TablerosSerializer

#models
from .models import Tableros

class TablerosCreate(APIView):
    def post(self, request):
        print(request.data)
        tablero_serializer = TablerosSerializer(data= request.data)
        if tablero_serializer.is_valid():
            tablero_serializer.save()
            return Response({"status": "ok", "description":"Tablero creado correctamente", "data":tablero_serializer.data}, status.HTTP_201_CREATED)
        else:
            return Response(tablero_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class TablerosModify(APIView):
    def put(self, request, pk):
        print(request.data)
        try:
            tablero = Tableros.objects.get(pk=pk)
        except Tableros.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        tablero_serializer = TablerosSerializer(tablero, data= request.data)
        if tablero_serializer.is_valid():
            tablero_serializer.save()
        return Response({"status": "ok", "description":"Tablero actualiza correctamente."}, status.HTTP_200_OK)
    
    def delete(self, request, pk):
        print(request.data)
        try:
            tablero = Tableros.objects.get(pk=pk)
        except Tableros.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        tablero.delete()
        return Response({"status": "ok", "description":"Tablero eliminado."}, status=status.HTTP_204_NO_CONTENT)
    