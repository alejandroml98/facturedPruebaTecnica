#Librerias
from rest_framework.response import Response # type: ignore
from rest_framework.views import APIView # type: ignore
from rest_framework import status

#serializers
from .serializer import TablerosSerializer

#models
from .models import Tableros

#services
from .services import rabbitmq_data_transform

#rabbitmq
from .rabbitmq_producer import send_message

class TablerosCreate(APIView):
    def post(self, request):
        tablero_serializer = TablerosSerializer(data= request.data)
        if tablero_serializer.is_valid():
            tablero_serializer.save()
            #enviar datos por rabbitmq a mongo
            rabbitmq_data = rabbitmq_data_transform("post", "tableros", tablero_serializer.data, None)
            send_message(rabbitmq_data)
            return Response({"status": "ok", "description":"Tablero creado correctamente", "data":tablero_serializer.data}, status.HTTP_201_CREATED)
        else:
            return Response(tablero_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class TablerosModify(APIView):
    def put(self, request, pk):
        try:
            tablero = Tableros.objects.get(pk=pk)
        except Tableros.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        tablero_serializer = TablerosSerializer(tablero, data= request.data)
        if tablero_serializer.is_valid():
            tablero_serializer.save()
            #enviar datos por rabbitmq a mongo
            rabbitmq_data = rabbitmq_data_transform("put", "tableros", tablero_serializer.data, None)
            send_message(rabbitmq_data)
        else:
            return Response(tablero_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"status": "ok", "description":"Tablero actualiza correctamente.","data":tablero_serializer.data}, status.HTTP_200_OK)
    
    def delete(self, request, pk):
        try:
            tablero = Tableros.objects.get(pk=pk)
        except Tableros.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        tablero_serializer = TablerosSerializer(tablero)
        rabbitmq_data = rabbitmq_data_transform("delete", "tableros", tablero_serializer.data, None)
        tablero.delete()
        send_message(rabbitmq_data)
        return Response({"status": "ok", "description":"Tablero eliminado."}, status=status.HTTP_204_NO_CONTENT)
    