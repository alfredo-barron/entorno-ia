# 🌸 Clasificación de Flores Iris usando Clasificador Bayesiano  

Este proyecto es un **ejemplo educativo de Machine Learning** utilizando el dataset Iris y un **clasificador Naive Bayes**, ejecutable en **tres entornos**:

- **Máquina local (host)**
- **Máquina virtual (Ubuntu en VirtualBox/VMware)**
- **Contenedor Docker**

---

## 📌 Objetivos del proyecto


- Implementar un clasificador Bayesiano en Python.
- Ejecutar y evaluar modelos de ML en **diferentes entornos de virtualización**.
- Medir y comparar **eficiencia de recursos** (CPU, RAM, tiempo).
- Analizar ventajas y desventajas de **local, VM y contenedor**.

---

## 🛠 Tecnologías utilizadas

- Python 3  
- scikit-learn  
- numpy, pandas, matplotlib  
- VirtualBox o VMware (para la VM con Ubuntu)  
- Docker  

---

## 📂 Contenido del repositorio

| Archivo | Descripción |
|---------|-------------|
| `iris_naive_bayes.py` | Script con clasificador Bayesiano. |
| `requirements.txt` | Dependencias necesarias. |
| `Dockerfile` | Definición del contenedor. |
| `README.md` | Documentación del proyecto. |

---

# 🔹 Ejecución en diferentes entornos

## 1️⃣ Ejecución en máquina local (Windows/Linux/Mac)

### 💾 Requisitos
- Python 3 instalado.  
- pip instalado.  

### 🚀 Pasos

1. Clonar el repositorio:

```bash
git clone https://github.com/alfredo-barron/entorno-ia.git
cd entorno-ia
```

2. Crear y activar entorno virtual:

```bash
python3 -m venv entorno-ia
source entorno-ia/bin/activate   # Linux/Mac
entorno-ia\Scripts\activate      # Windows
```

3.	Instalar dependencias

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

## 2️⃣ Ejecución en máquina virtual Ubuntu (VirtualBox/VMware)

### 💾 Requisitos
- VirtualBox o VMware instalado.  
- Imagen de Ubuntu 25.04 LTS.  
- Conexión a Internet dentro de la VM.

### 🚀 Pasos

1.	Crear una VM con al menos:

- RAM: **4 GB**
- CPU: **2 núcleos**
- Disco: **25 GB**

2. Iniciar la VM, actualizar repositorios e instalar dependencias de Python:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-venv python3-pip git -y
```

3. Clonar el repositorio en la VM:

```bash
git clone https://github.com/alfredo-barron/entorno-ia.git
cd entorno-ia
```

4. Crear entorno virtual e instalar dependencias:

```bash
python3 -m venv entorno-ia
source entorno-ia/bin/activate
pip install -r requirements.txt
```

5. Ejecutar el script:

```bash
python iris_naive_bayes.py
```

✅ La salida debe ser la misma que en el entorno local.

## 3️⃣ Ejecución en Docker

### 💾 Requisitos
- Docker instalado.

### 🚀 Pasos

1. Construir la imagen:

```bash
docker build -t iris-bayes .
```

2. Ejecutar el contenedor:

```bash
docker run --rm iris-bayes
```

✅ La salida será la misma que en los otros entornos.

## 📊 Medición de consumo de recursos

El objetivo es comparar eficiencia en los tres entornos.

### 🖥️ Local (host)

- Ejecutar:

```bash
time python iris_naive_bayes.py
top      # o htop
ps aux | grep python
```

### 💻 Máquina virtual (Ubuntu)

- Dentro de la VM:

```bash
time python3 iris_naive_bayes.py
top / htop
```

- Desde el host: observar el consumo global de la VM en el Administrador de tareas / Monitor del sistema.

### 🐳 Contenedor Docker

- Ejecutar el contenedor:

```bash
docker run --rm --name iris-test iris-bayes
```

- En otra terminal:

```bash
docker stats iris-test
```

### 📑 Registro sugerido

- CPU (%)
- RAM (MB)
- Tiempos
- Observaciones

## 📚 Referencias

- Dataset Iris – scikit-learn: https://scikit-learn.org/stable/datasets/toy_dataset.html#iris-plants-dataset
- Naive Bayes – scikit-learn: https://scikit-learn.org/stable/modules/naive_bayes.html
- Documentación oficial de Docker: https://docs.docker.com/

## ⚡ Notas para estudiantes
- Ejecutar este proyecto en local, VM y Docker permite comparar:
	- Rendimiento
	- Uso de recursos
	- Facilidad de despliegue
- Esto sirve como base para llevar proyectos de IA a la nube.