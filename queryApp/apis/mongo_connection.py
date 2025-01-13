from pymongo import MongoClient
client = MongoClient()

client = MongoClient("mongodb", 27017)
db = client.db_test

def prueba():
    collection = db.tests
    return collection.find()