# model.py

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import database

class Model:
    def __init__(self):
        self.models = {}

    def create_model(self, model_data):
        model_name = model_data['name']
        model_type = model_data['type']
        model_params = model_data['params']

        if model_type == 'sequential':
            model = keras.Sequential()
            for layer in model_params['layers']:
                if layer['type'] == 'dense':
                    model.add(layers.Dense(layer['units'], activation=layer['activation']))
                elif layer['type'] == 'dropout':
                    model.add(layers.Dropout(layer['rate']))
                elif layer['type'] == 'conv2d':
                    model.add(layers.Conv2D(layer['filters'], layer['kernel_size'], activation=layer['activation']))
                elif layer['type'] == 'maxpooling2d':
                    model.add(layers.MaxPooling2D(layer['pool_size']))
                elif layer['type'] == 'flatten':
                    model.add(layers.Flatten())
            model.compile(optimizer=model_params['optimizer'], loss=model_params['loss'], metrics=model_params['metrics'])
        else:
            raise ValueError('Unsupported model type')

        self.models[model_name] = model
        database.insert_data('models', {'name': model_name, 'type': model_type, 'params': model_params})

        return {'status': 'success', 'message': 'Model created successfully'}

    def get_model(self, model_name):
        if model_name in self.models:
            return self.models[model_name]
        else:
            raise ValueError('Model not found')

    def update_model(self, model_name, new_params):
        if model_name in self.models:
            model = self.models[model_name]
            model.compile(optimizer=new_params['optimizer'], loss=new_params['loss'], metrics=new_params['metrics'])
            database.update_data('models', {'name': model_name}, {'params': new_params})
            return {'status': 'success', 'message': 'Model updated successfully'}
        else:
            raise ValueError('Model not found')

    def delete_model(self, model_name):
        if model_name in self.models:
            del self.models[model_name]
            database.delete_data('models', {'name': model_name})
            return {'status': 'success', 'message': 'Model deleted successfully'}
        else:
            raise ValueError('Model not found')

model = Model()

def create_model(model_data):
    return model.create_model(model_data)

def get_model(model_name):
    return model.get_model(model_name)

def update_model(model_name, new_params):
    return model.update_model(model_name, new_params)

def delete_model(model_name):
    return model.delete_model(model_name)
