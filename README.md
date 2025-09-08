# Clasificación de Flores Iris usando Clasificador Bayesiano en Docker

Este proyecto es un **ejemplo educativo de Machine Learning** utilizando el dataset Iris y un **clasificador Naive Bayes**, ejecutable dentro de un contenedor Docker.

---

## 📌 Objetivos del proyecto

- Implementar un clasificador Bayesiano en Python.
- Ejecutar y evaluar modelos de ML en **contenedores**, simulando entornos en la nube.
- Comparar ejecución en **entorno local, VM y contenedor Docker**.

---

## 🛠 Tecnologías utilizadas

- Python 3
- scikit-learn
- numpy, pandas, matplotlib
- Docker

---

## 💾 Requisitos

- Tener **Docker** instalado: [https://www.docker.com/get-started](https://www.docker.com/get-started)

---

## 📂 Contenido del repositorio

| Archivo | Descripción |
|---------|-------------|
| `iris_naive_bayes.py` | Script con clasificador Bayesiano. |
| `requirements.txt` | Dependencias necesarias. |
| `Dockerfile` | Definición del contenedor. |
| `README.md` | Documentación del proyecto. |

---

## 💾 Requisitos

- Python 3 instalado.
- Instalar librerías:

```bash
pip install -r requirements.txt
```

## 🚀 Cómo ejecutar el proyecto

1. Clonar el repositorio:

```bash
git clone https://github.com/alfredo-barron/entorno-ia.git
cd entorno-ia
```

2. Crear y activar entorno virtual

```bash
python3 -m venv entorno-ia
source entorno-ia/bin/activate   # Linux/Mac
entorno-ia\Scripts\activate      # Windows
```

3.	Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Ejecutar script:

```bash
python iris_naive_bayes.py
```

5. Salida esperada:

```bash
Exactitud del modelo: 0.9667
Reporte de clasificación:
              precision    recall  f1-score   support
setosa           1.00      1.00      1.00         10
versicolor       0.92      1.00      0.96         11
virginica        1.00      0.91      0.95         11
Matriz de confusión:
[[10  0  0]
 [ 0 11  0]
 [ 0  1 10]]
```

## 🚀 Cómo ejecutar en Docker

1. Construir la imagen:

```bash
docker build -t iris-bayes .
```

2. Ejecutar el contenedor:

```bash
docker run --rm iris-bayes
```

5. Salida esperada:

```bash
Exactitud del modelo: 0.9667
Reporte de clasificación:
              precision    recall  f1-score   support
setosa           1.00      1.00      1.00         10
versicolor       0.92      1.00      0.96         11
virginica        1.00      0.91      0.95         11
Matriz de confusión:
[[10  0  0]
 [ 0 11  0]
 [ 0  1 10]]
```