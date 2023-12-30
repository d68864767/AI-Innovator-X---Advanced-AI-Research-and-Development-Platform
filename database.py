# database.py

from pymongo import MongoClient

class Database:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['ai_innovator_x']

    def insert_data(self, collection_name, data):
        collection = self.db[collection_name]
        result = collection.insert_one(data)
        return result.inserted_id

    def get_data(self, collection_name, query={}):
        collection = self.db[collection_name]
        result = collection.find(query)
        return list(result)

    def update_data(self, collection_name, query, new_data):
        collection = self.db[collection_name]
        result = collection.update_one(query, {'$set': new_data})
        return result.modified_count

    def delete_data(self, collection_name, query):
        collection = self.db[collection_name]
        result = collection.delete_one(query)
        return result.deleted_count

database = Database()

def insert_data(collection_name, data):
    return database.insert_data(collection_name, data)

def get_data(collection_name, query={}):
    return database.get_data(collection_name, query)

def update_data(collection_name, query, new_data):
    return database.update_data(collection_name, query, new_data)

def delete_data(collection_name, query):
    return database.delete_data(collection_name, query)
