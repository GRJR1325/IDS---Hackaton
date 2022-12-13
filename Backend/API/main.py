import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
from joblib import dump, load
from fastapi import FastAPI
from fastapi import status
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from joblib import load
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


class Features(BaseModel):
    exp: int
    node: int
    sql: int
    postgsql: int
    aws: int
    js: int
    ningles: float
    visap: int
    hofice: int
    estudios: int

    class Config:
        schema_extra = {
            "example": {
                "exp": 5,
                "node": 6,
                "sql": 8,
                "postgsql": 2,
                "aws": 6,
                "js": 6,
                "ningles": 43.5,
                "visap": 1,
                "hofice": 1,
                "estudios": 15
            }
        }


class Label(BaseModel):
    hiring: float


class message(BaseModel):
    message: float


app = FastAPI()


@app.post(
    "/hiring/",
    response_model=Label,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Predecir la probabilidad de ser contratado",
    description="Predecir la probabilidad de ser contratado",
    tags={"Predictive hiring model"}
)
async def get_hiring(features: Features):
    try:
        model = load('model.joblib')
        data = [
            features.exp,
            features.node,
            features.sql,
            features.postgsql,
            features.aws,
            features.js,
            features.ningles,
            features.visap,
            features.hofice,
            features.estudios
        ]
        predictions = model.predict([data])
        conexionBaseDatos(data, predictions[0])
        response = {"hiring": predictions[0]}
        return response
    except Exception as e:
        response = JSONResponse(
            status_code=400,
            content={"message": f"{e.args}"},
        )
        return response


hiring_model = pd.read_csv("works_oferts.csv")
# print(hiring_model)
X = hiring_model[['exp', 'node', 'sql', 'postgsql', 'aws',
                  'js', 'ningles', 'visap', 'hofice', 'estudios']].values
y = hiring_model['probabilidad'].values
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=0)


model_load = load('model.joblib')
predictions = model_load.predict(X_test)
# print(predictions[:2])
cred = credentials.Certificate(
    'hiring-e6eec-firebase-adminsdk-wqgvr-64d77be9d6.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://hiring-e6eec-default-rtdb.firebaseio.com/"
})


def conexionBaseDatos(data, predictions):
    ref = db.reference('/')
    datos = {
        "exp": data[0],
        "node": data[1],
        "sql": data[2],
        "postgsql": data[3],
        "aws": data[4],
        "js": data[5],
        "ningles": data[6],
        "visap": data[7],
        "hofice": data[8],
        "estudios": data[9],
        "predictions": predictions
    }
    ref.push(datos)
    print(ref.get("/"))
