# collaboration.py

from database import insert_data, get_data, update_data, delete_data

class Collaboration:
    def __init__(self):
        self.collection_name = 'collaboration'

    def create_project(self, data):
        return insert_data(self.collection_name, data)

    def get_project(self, query={}):
        return get_data(self.collection_name, query)

    def update_project(self, query, new_data):
        return update_data(self.collection_name, query, new_data)

    def delete_project(self, query):
        return delete_data(self.collection_name, query)

collaboration = Collaboration()

def collaborate(data):
    action = data.get('action')

    if action == 'create':
        return collaboration.create_project(data.get('data'))
    elif action == 'get':
        return collaboration.get_project(data.get('query'))
    elif action == 'update':
        return collaboration.update_project(data.get('query'), data.get('new_data'))
    elif action == 'delete':
        return collaboration.delete_project(data.get('query'))
    else:
        return {'error': 'Invalid action'}
