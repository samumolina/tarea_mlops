import pickle
import numpy as np

# Cargar modelo
with open("modelo.pkl", "rb") as f:
    modelo = pickle.load(f)

# ejemplo de entrada (como el dataset de Iris)
ejemplo = np.array([5.1, 3.5, 1.4, 0.2]).reshape(1, -1)

# predicción
prediccion = modelo.predict(ejemplo)

print(f"La predicción es: {prediccion[0]}")
