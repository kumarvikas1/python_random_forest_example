from temp_destination.controller.model_executor import ModelExecutor
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib as lib
import pandas as pd
import os as OS
from abc import ABC, abstractmethod
from sanic.response import json

class RandomForestRegression(ModelExecutor) :

    model = ''
    def __init__(self):
        self.model = lib.load("/opt/models/random_forest/test_model_save.pkl")


    def executeModel(self, request):
        #features_predict= pd.read_csv('/Users/vikakumar/Desktop/test_ml_ola_predict.csv')
        req = pd.read_json(request.body)
        #print(features_predict.to_json(orient='records'))
        return self.model.predict(req).tolist()