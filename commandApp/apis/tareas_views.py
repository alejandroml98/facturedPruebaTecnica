#Librerias
from rest_framework.response import Response # type: ignore
from rest_framework.views import APIView # type: ignore
from rest_framework import status

#serializers
from .serializer import TareasSerializer

#models
from .models import Tareas

class TareasCreate(APIView):
    def post(self, request):
        print(request.data)
        tarea_serializer = TareasSerializer(data= request.data)
        if tarea_serializer.is_valid():
            tarea_serializer.save()
            return Response({"status": "ok", "description":"Tarea creada correctamente", "data":tarea_serializer.data}, status.HTTP_201_CREATED)
        else:
            return Response(tarea_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class TareasModify(APIView):
    def put(self, request, pk):
        print(request.data)
        try:
            Tarea = Tareas.objects.get(pk=pk)
        except Tareas.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        tarea_serializer = TareasSerializer(Tarea, data= request.data)
        if tarea_serializer.is_valid():
            tarea_serializer.save()
            return Response({"status": "ok", "description":"Tarea actualiza correctamente.", "data": tarea_serializer.data}, status.HTTP_200_OK)
        else:
            return Response(tarea_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        print(request.data)
        try:
            Tarea = Tareas.objects.get(pk=pk)
        except Tareas.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        Tarea.delete()
        return Response({"status": "ok", "description":"Tarea eliminado."}, status=status.HTTP_204_NO_CONTENT)
    