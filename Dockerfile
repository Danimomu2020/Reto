# Usa una imagen base de Python con la versión que estés utilizando (ejemplo: 3.9)
FROM python:3.9

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de requirements y los instala
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY . /app/

# Aplica las migraciones de Django
RUN python manage.py migrate

# Intento de ejecutar la importación de datos del NIST (opcional para depuración)
RUN python manage.py import_nist

# Expone el puerto en el que la aplicación Django se ejecutará
EXPOSE 8000

# Comando para ejecutar la aplicación Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]