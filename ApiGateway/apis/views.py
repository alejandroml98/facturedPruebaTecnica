#Librerias
from rest_framework.response import Response # type: ignore
from rest_framework.views import APIView # type: ignore
from rest_framework import status

import requests

class Prueba(APIView):
    def get(self, request):
        url = "http://querysApp:8000"+ request.path
        query_params = request.query_params
        respuesta =requests.get(url, params=query_params)
        if respuesta.status_code == 200:
            return Response(respuesta.json())
        else:
            return Response({"info": respuesta.text},respuesta.status_code)
        
    
    def post(self, request):
        url = "http://commandsApp:8000"+ request.path
        query_params = request.query_params
        respuesta =requests.post(url, data=request.data, params=query_params)
        if respuesta.status_code in [200, 201]:
            return Response(respuesta.json())
        else:
            return Response({"info": respuesta.text},respuesta.status_code)
        
    def put(self, request):
        url = "http://commandsApp:8000"+ request.path
        query_params = request.query_params
        respuesta =requests.put(url, data=request.data, params=query_params)
        if respuesta.status_code == 200:
            return Response(respuesta.json())
        else:
            return Response({"info": respuesta.text},respuesta.status_code)
        
    def delete(self, request):
        url = "http://commandsApp:8000"+ request.path
        query_params = request.query_params
        respuesta =requests.delete(url, data=request.data, params=query_params)
        if respuesta.status_code in [204]:
            print(respuesta)
            return Response({"info": "eliminado correctamente"}, respuesta.status_code)
        else:
            return Response({"info": respuesta.text},respuesta.status_code)