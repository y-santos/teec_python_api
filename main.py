from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
from flask import Flask, jsonify, request
from flask_restful import Resource

df = pd.read_csv('./dados.csv')
df_clean = df.dropna()

X=df_clean[['Wind', 'Temp', 'Month']]
y=df_clean['Ozone']

model = LinearRegression()
model.fit(X, y)

class modeloLM(Resource):
    def get(self, wind, temp, month):
        #obter inputs via query string
        wind = float(wind)
        temp = float(temp)
        month = int(mont)

        #prever
        predicao = model.predict([[wind, temp, month]])

        return jsonify({
            'predited_Ozone': predicao[0]
        })

