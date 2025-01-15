from ast import Global
import json
import os
from .rabbitmq_connection import RabbitmqConn
rabbitmq_cola = os.getenv('RABBITMQ_QUEUE', 'db_sync_queue')

conn = None
channel = None 


def send_message(mensaje):
    global conn
    global channel
    if conn is None or conn.is_closed:
        conn = RabbitmqConn().get_conn()
        channel = conn.channel()
        channel.queue_declare(queue=rabbitmq_cola)
        
    channel.basic_publish(exchange='',routing_key=rabbitmq_cola, body= json.dumps(mensaje))
    print("mensaje enviado a rabbitmq")
    
    


#connection.close()



#Tableros.objects.prefetch_related('tareas').get(pk=1)