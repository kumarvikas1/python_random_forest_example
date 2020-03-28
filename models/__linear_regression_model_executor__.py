from temp_destination.controller.model_executor import ModelExecutor
import numpy as np
from sklearn.linear_model import LinearRegression
from abc import ABC, abstractmethod
from sanic.response import json

class LinearRegressionModelExecutor(ModelExecutor) :
    def executeModel(self):
        x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
        y = np.array([10, 30, 50, 70, 90, 110])
        model = LinearRegression()
        model.fit(x, y)
        r_sq = model.score(x, y)
        y_pred = model.predict(np.array([9,78,67,88,92]).reshape(-1,1))
        return y_pred
