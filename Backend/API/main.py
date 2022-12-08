from fastapi import FastAPI
from fastapi import status
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from joblib import load
from fastapi.middleware.cors import CORSMiddleware
import os

data_set = os.path.join("model.joblib")

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def get_saludo():
    mensaje = {"Hola": "Mundo"}
    return mensaje


@app.post('/test/{experiencia}/{node}/{sql}/{postgsql}/{aws}/{js}/{ningles}/{visap}/{hofice}/{estidios}',
          status_code=status.HTTP_202_ACCEPTED,
          summary="Get a prediction",
          description="Get a prediction",
          tags=["auth"])
async def post_datos(experiencia: int, node: int, sql: int, postgsql: int, aws: int, js: int, ningles: float, visap: int, hofice: int, estidios: int):
    model = load(data_set)
    data = [experiencia, node, sql, postgsql,
            aws, js, ningles, visap, hofice, estidios]
    prediction = model.predict([data])
    mensaje = "tu probabilidad de ser contratado es de: "+str(prediction[0])
    return mensaje
