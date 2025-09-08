import time
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# 📌 Cargar dataset Iris
iris = datasets.load_iris()
X, y = iris.data, iris.target

# 📌 Aumentar tamaño del dataset (duplicar 1000 veces)
X = np.tile(X, (1000, 1))
y = np.tile(y, 1000)

# 📌 Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 📌 Inicializar clasificador
model = GaussianNB()

# Medir tiempo de ejecución
start = time.time()

# 📌 Repetir entrenamiento varias veces para aumentar carga
for _ in range(200):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

end = time.time()

# 📌 Métricas
print("Exactitud del modelo:", accuracy_score(y_test, y_pred))
print("\nReporte de clasificación:\n", classification_report(y_test, y_pred))
print("Matriz de confusión:\n", confusion_matrix(y_test, y_pred))

# 📌 Tiempo total
print(f"\n⏱️ Tiempo de ejecución: {end - start:.2f} segundos")

# 📌 Simulación de carga adicional (matriz grande)
print("\nEjecutando cálculos adicionales para simular carga...")
A = np.random.rand(3000, 3000)
B = np.random.rand(3000, 3000)
C = A @ B   # Multiplicación de matrices pesadas
print("✅ Cálculo adicional completado (matriz 3000x3000).")