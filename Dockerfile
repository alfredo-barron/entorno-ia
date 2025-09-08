# Usar imagen oficial de Python
FROM python:3.11-slim

# Información del autor
LABEL maintainer="alfredo.barron@tecvalles.mx"

# Crear directorio de trabajo
WORKDIR /app

# Copiar requirements y script
COPY requirements.txt .
COPY iris_naive_bayes.py .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto al iniciar el contenedor
CMD ["python", "iris_naive_bayes.py"]