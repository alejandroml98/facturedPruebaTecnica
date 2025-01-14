from pymongo import MongoClient
class MongoDBClient:
    _instance = None  # Variable de clase para almacenar la instancia única

    def __new__(cls, uri, database_name,*args, **kwargs):
        if not cls._instance:  # Verifica si ya existe una instancia
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, uri, database_name):
        if not hasattr(self, "_initialized"):  # Evita reconfiguración en nuevas llamadas
            self._initialized = True
            self.client = MongoClient(uri)
            self.database = self.client[database_name]

    def get_collection(self, collection_name):
        """
        Obtiene una colección de la base de datos.
        """
        return self.database[collection_name]