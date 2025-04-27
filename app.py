import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

# Cargar modelo
with open("modelo.pkl", "rb") as f:
    modelo = pickle.load(f)

# Crear app
app = FastAPI()

# input esperado
class InputData(BaseModel):
    features: list

# Ruta principal
@app.get("/")
def root():
    return {"message": "API está funcionando"}

# Ruta de predicción
@app.post("/predict")
def predict(data: InputData):
    input_array = np.array(data.features).reshape(1, -1)
    prediction = modelo.predict(input_array)
    return {"prediction": int(prediction[0])}
