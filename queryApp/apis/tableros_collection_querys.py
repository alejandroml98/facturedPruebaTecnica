from .mongo_connection import MongoDBClient

mongo_client = MongoDBClient(uri="mongodb://mongodb:27017/", database_name="facturedtest")

tableros_collection= mongo_client.get_collection("tableros_collection")


def list_all_tableros(skip, page_size, con_tareas):
    projection= {}
    if con_tareas == 0:
        projection = {"tareas":0}

    return tableros_collection.find({},projection).skip(skip).limit(page_size)

def get_tarea(id):
    return tableros_collection.find_one({"_id":id})

def count_all():
    return tableros_collection.count_documents({})