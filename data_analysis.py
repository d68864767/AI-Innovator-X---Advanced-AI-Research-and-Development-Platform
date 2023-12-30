# data_analysis.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import database

class DataAnalysis:
    def __init__(self):
        pass

    def load_data(self, collection_name, query={}):
        data = database.get_data(collection_name, query)
        df = pd.DataFrame(data)
        return df

    def preprocess_data(self, df, missing_values='mean', scale_data=False):
        if missing_values == 'mean':
            df.fillna(df.mean(), inplace=True)
        elif missing_values == 'median':
            df.fillna(df.median(), inplace=True)
        elif missing_values == 'mode':
            df.fillna(df.mode().iloc[0], inplace=True)

        if scale_data:
            from sklearn.preprocessing import StandardScaler
            scaler = StandardScaler()
            df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

        return df

    def visualize_data(self, df, plot_type='histogram'):
        if plot_type == 'histogram':
            df.hist(bins=50, figsize=(20,15))
            plt.show()
        elif plot_type == 'correlation_matrix':
            corr_matrix = df.corr()
            plt.figure(figsize=(12, 9))
            sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
            plt.show()
        else:
            raise ValueError('Unsupported plot type')

data_analysis = DataAnalysis()

def load_data(collection_name, query={}):
    return data_analysis.load_data(collection_name, query)

def preprocess_data(df, missing_values='mean', scale_data=False):
    return data_analysis.preprocess_data(df, missing_values, scale_data)

def visualize_data(df, plot_type='histogram'):
    return data_analysis.visualize_data(df, plot_type)
