#Clase para conexión con rabbitmq
import os
import pika

class RabbitmqConn:
    #Atributos de clase
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, conn=None):
        if not hasattr(self, "initialized"):  # Evitar reconfiguración en múltiples llamadas
            self.initialized = True
            self.conn = conn
    
    def create_conn(self):
        rabbitmq_host= os.getenv('RABBITMQ_HOST', 'rabbitmqfr')
        #Host de rabbitmq
        connections_parameters = pika.ConnectionParameters(rabbitmq_host,heartbeat=600,blocked_connection_timeout=300)
        connection = pika.BlockingConnection(connections_parameters)
        print("creando conexion rabbitmq")
        self.conn = connection

    def get_conn(self):
        if None is self.conn or self.conn.is_closed:
            self.create_conn()
        print("retornando conexion rabbitmq")
        return self.conn
    
    def close_conn(self):
        if None is not self.conn:
            self.conn.close()
            print("cerrando conexion rabbitmq")