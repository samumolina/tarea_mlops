# imagen base de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos necesarios al contenedor
COPY requirements.txt . 
COPY app.py . 
COPY modelo.pkl .

# Instalar las dependencias de la app
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el que correrá la app
EXPOSE 8000

# Comando para iniciar la aplicación
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
