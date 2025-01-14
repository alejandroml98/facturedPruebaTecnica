from .mongo_connection import MongoDBClient

mongo_client = MongoDBClient(uri="mongodb://mongodb:27017/", database_name="facturedtest")

tareas_collection= mongo_client.get_collection("tareas_collection")


def list_all_tareas(skip, page_size):
    return tareas_collection.find({}).skip(skip).limit(page_size)

def get_tarea(id):
    return tareas_collection.find_one({"_id":id})

def count_all(id_tablero= None):
    filter = {}
    if id_tablero is not None:
        filter["id_tablero"]= id_tablero
    return tareas_collection.count_documents(filter)

def count_tarea_by_estado_and_tablero(estado, id_tablero):
    filter = {"estado": estado}
    if id_tablero is not None:
        filter["id_tablero"]= id_tablero
    
    return tareas_collection.count_documents(filter)
