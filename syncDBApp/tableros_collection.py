from mongodb_connection import MongoDBClient
mongo_client = MongoDBClient(uri="mongodb://mongodb:27017/", database_name="facturedtest")

tableros_collection= mongo_client.get_collection("tableros_collection")
tareas_collection= mongo_client.get_collection("tareas_collection")


def tableros_collection_controller(rabbitmq_mensaje):
    print("iniciando tableros_collecion procesamiento")
    metodo = rabbitmq_mensaje["metodo"]
    tabla = rabbitmq_mensaje["tabla"]
    tareas_data = rabbitmq_mensaje["tareas_data"]
    tableros_data = rabbitmq_mensaje["tableros_data"]

    if metodo == 'post':
        if tabla=='tareas': 
            update_document(rabbitmq_mensaje)
        else: #para tabla tableros y seeder
            insert_document(tableros_data)
        
    if metodo == "put":        
        update_document(rabbitmq_mensaje)
    
    if metodo == "delete":
        if tabla == "tableros":
            delete_document(tableros_data)
        if tabla == "tareas":
            update_document(rabbitmq_mensaje)


def insert_document(tableros_data):
    print("tableros: insertando")
    tableros_collection.insert_one(tableros_data)

def update_document(rabbitmq_mensaje):
    print("tableros: actualizando")
    if rabbitmq_mensaje["tabla"] =="tableros":
        query = {"_id" : rabbitmq_mensaje["tableros_data"]["_id"]}
        new_values = {"$set":rabbitmq_mensaje["tableros_data"]}
        tableros_collection.update_one(query, new_values)
    else:
        query = {"_id" : rabbitmq_mensaje["tareas_data"]["id_tablero"]}
        tarea_data = rabbitmq_mensaje["tareas_data"]
        if rabbitmq_mensaje["metodo"]== "post":          
            #print("insertando a tareas embebido")  
            push_value = {"$push": {"tareas": tarea_data}}
            tableros_collection.update_one(query, push_value)

        if rabbitmq_mensaje["metodo"]== "put":
            #Validar si hubo cambio de tablero
            old_tarea = tareas_collection.find_one({"_id":tarea_data["_id"]})
            if old_tarea["id_tablero"] != tarea_data["id_tablero"]:
                #remover tarea de lista del tablero viejo
                pull_value={"$pull": {"tareas": {"_id":tarea_data["_id"]}}}
                tableros_collection.update_one({"_id" : old_tarea["id_tablero"]}, pull_value)
                #agregar a nuevo tablero
                push_value = {"$push": {"tareas": tarea_data}}
                tableros_collection.update_one({"_id" : tarea_data["id_tablero"]}, push_value)
            else:
                set_value = {"$set": {"tareas.$[tarea]":tarea_data}}
                array_filter = [{ "tarea._id": tarea_data["_id"] }]
                tableros_collection.update_one(filter=query, update=set_value, array_filters=array_filter)

        if rabbitmq_mensaje["metodo"]== "delete":
            id = tarea_data["_id"]
            print(tarea_data)
            pull_value={"$pull": {"tareas": {"_id":id}}}
            tableros_collection.update_one(query, pull_value)

def delete_document(tableros_data):
    print("tableros: eliminando")
    query = {"_id": tableros_data["_id"]}
    tableros_collection.delete_one(query)
