import json
import pika
import os

from tableros_collection import tableros_collection_controller
from tareas_collection import tareas_collection_controller

def on_message_received(ch, method, properties, body):
    print("Se recibio un mensaje")
    try:
        mensaje = json.loads(body)
        tareas_transform_id_key(mensaje["tareas_data"])
        tableros_transform_id_key(mensaje["tableros_data"])
        print(mensaje)
        tableros_collection_controller(mensaje)
        tareas_collection_controller(mensaje)
    except Exception as e:
        print(e)

def tareas_transform_id_key(tareas_data):
    if tareas_data is not None:
        tareas_data["_id"]= tareas_data.pop("id")

def tableros_transform_id_key(tableros_data):
    if tableros_data is not None:
        tableros_data["_id"]= tableros_data.pop("id")
        if "tareas" in tableros_data:
            for tarea in tableros_data["tareas"]:
                tarea["_id"]= tarea.pop("id")


rabbitmq_host= os.getenv('RABBITMQ_HOST', 'rabbitmqfr')
rabbitmq_cola = os.getenv('RABBITMQ_QUEUE', 'db_sync_queue')

#Host de rabbitmq
connections_parameters = pika.ConnectionParameters(rabbitmq_host, heartbeat=600,blocked_connection_timeout=300)

#Crear conexion 
connection = None
connection = pika.BlockingConnection(connections_parameters)
#print(connection)
#print(connection is None)

#canal
channel = connection.channel()
#Selecciona un canal y lo crea si es necesario
channel.queue_declare(queue=rabbitmq_cola)

channel.basic_consume(queue=rabbitmq_cola, auto_ack=True, on_message_callback=on_message_received)

print("escuchando")

channel.start_consuming()