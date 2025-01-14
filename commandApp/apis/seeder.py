#librerias python
import random
import concurrent.futures
from faker import Faker
#models
from apis.models import Tableros, Tareas

#Enums 
from apis.enums import EstadostareaEnum

#Serializer
from apis.serializer import TablerosSerializer, TareasSerializer, TableroConTareasSerializer

#Services
from apis.services import rabbitmq_data_transform
from apis.rabbitmq_producer import send_message

def seed(cantidad_tableros, cantidad_tareas):
    tableros_data = seeder_tableros(cantidad_tableros)
    lista_id_tableros = [o["id"] for o in tableros_data]
    
    # Creando pool de hilos para insertar numeros
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        total_tareas= cantidad_tareas
        tareas_hilo= 5_000
        repeticiones = int(total_tareas/tareas_hilo)
        futures = []
        for i in range(repeticiones):
            print(i)
            futures.append(executor.submit(seeder_tareas, tareas_hilo, lista_id_tableros))
        
        # Esperar a que terminen todas las tareas
        concurrent.futures.wait(futures)
        for future in futures:
            print(future.result())

        print("finalizando seeder.")
        seeder_sync_rabbitmq()
        print("finalizando seeder mongodb.")
    


def seeder_tableros(cantidad_tableros):
    faker = Faker()
    tableros_data = []
    for i in range(cantidad_tableros):
        data = {
            "nombre": "Tablero "+ faker.name(),
            "descripcion": "Descripcion "+ faker.text(30)
        }
        tableros_data.append(data)
    
    tablero_serializer = TablerosSerializer(data= tableros_data, many=True)
    if tablero_serializer.is_valid():
        tablero_serializer.save()
        return tablero_serializer.data
    else:
        return None

def seeder_tareas(cantidad_tareas, lista_tableros):
    print("iniciando inserción tareas")
    faker = Faker()
    tareas_data = []
    for i in range(cantidad_tareas):
        data = {
            "titulo": "Titulo "+ faker.name(),
            "descripcion": "Descripcion "+ faker.text(30),
            "estado": random.choice([i.value for i in EstadostareaEnum]),
            "id_tablero": int(random.choice(lista_tableros))
        }
        tareas_data.append(data)
    
    print("serializando")
    tablero_serializer = TareasSerializer(data= tareas_data, many=True)
    print("final serialización")
    if tablero_serializer.is_valid():
        print("guardando")
        tablero_serializer.save()
        print("tareas insertadas")
    else:
        print("error")
    
def seeder_sync_rabbitmq():
    tableros_ids_list = Tableros.objects.all().values_list("id", flat=True)

    try:
        for id in tableros_ids_list:
            tablero=Tableros.objects.prefetch_related('tareas').get(pk=id)
            tablero_serializer = TableroConTareasSerializer(tablero)
            rabbitmq_data = rabbitmq_data_transform("post","seeder",tablero_serializer.data, None)
            send_message(rabbitmq_data)
        pass
    except Exception as e:
        print(e)


