# resources.py

import database

class Resources:
    def __init__(self):
        self.collection_name = 'resources'

    def add_resource(self, resource):
        return database.insert_data(self.collection_name, resource)

    def get_resources(self, query={}):
        return database.get_data(self.collection_name, query)

    def update_resource(self, query, new_data):
        return database.update_data(self.collection_name, query, new_data)

    def delete_resource(self, query):
        return database.delete_data(self.collection_name, query)

resources = Resources()

def add_resource(resource):
    return resources.add_resource(resource)

def get_resources(query={}):
    return resources.get_resources(query)

def update_resource(query, new_data):
    return resources.update_resource(query, new_data)

def delete_resource(query):
    return resources.delete_resource(query)
