import pickle
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Cargar datos de iris
iris = load_iris()
X, y = iris.data, iris.target

# Entrenar un modelo simple
modelo = RandomForestClassifier()
modelo.fit(X, y)

# Guardar el modelo entrenado en un archivo
with open("modelo.pkl", "wb") as f:
    pickle.dump(modelo, f)

print("Modelo entrenado y guardado como modelo.pkl")
