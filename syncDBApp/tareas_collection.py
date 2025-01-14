from mongodb_connection import MongoDBClient

mongo_client = MongoDBClient(uri="mongodb://mongodb:27017/", database_name="facturedtest")

tareas_collection= mongo_client.get_collection("tareas_collection")


def tareas_collection_controller(rabbitmq_mensaje):
    print("iniciando tareas_collecion procesamiento")
    metodo = rabbitmq_mensaje["metodo"]
    tabla = rabbitmq_mensaje["tabla"]
    tareas_data = rabbitmq_mensaje["tareas_data"]
    tableros_data = rabbitmq_mensaje["tableros_data"]

    if metodo == 'post':
        if tabla=='tareas': 
            insert_document(tareas_data)
        if tabla=="seeder": 
            insert_many_documents(tableros_data)
    
    if metodo == "put":
        update_document(tareas_data)
    
    if metodo == "delete":
        if tabla== "tareas":
            delete_document(tareas_data)
        if tabla == "tableros":
            delete_many(tableros_data)


def insert_document(tarea_data):
    print("tareas: insertando")
    tareas_collection.insert_one(tarea_data)

def insert_many_documents(tableros_data):
    print("tareas: insertando masivo")
    print(tableros_data)
    if "tareas" in tableros_data:
        if len(tableros_data["tareas"])>0:
            tareas_collection.insert_many(tableros_data["tareas"])

def update_document(tarea_data):
    print("tareas: actualizando")
    query = {"_id":tarea_data["_id"]}
    new_values = {"$set":tarea_data}
    tareas_collection.update_one(query, new_values)

def delete_document(tarea_data):
    print("tareas: eliminando")
    query = {"_id":tarea_data["_id"]}
    tareas_collection.delete_one(query)

def delete_many(tableros_data):
    print("tareas: eliminando varios")
    query = {"id_tablero":tableros_data["_id"]}
    tareas_collection.delete_many(query)

