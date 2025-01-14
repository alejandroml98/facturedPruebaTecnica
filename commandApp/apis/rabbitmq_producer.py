from ast import Global
import json
import os
from .rabbitmq_connection import RabbitmqConn
rabbitmq_cola = os.getenv('RABBITMQ_QUEUE', 'db_sync_queue')

conn = None
channel = None

#mensaje = "hola mundo"
def open_channel():
    #Selecciona un canal y lo crea si es necesario
    global channel
    channel = conn.channel()
    channel.queue_declare(queue=rabbitmq_cola)

def send_message(mensaje):
    check_conn()
    channel.basic_publish(exchange='',routing_key=rabbitmq_cola, body= json.dumps(mensaje))
    print("mensaje enviado a rabbitmq")

def check_conn():
    global conn
    if conn is None or conn.is_closed:
        conn = RabbitmqConn().get_conn()
        open_channel()




#connection.close()



#Tableros.objects.prefetch_related('tareas').get(pk=1)