Cómo Ejecutar la Aplicación

Tienes dos formas principales de poner en marcha esta aplicación en tu computadora: usando Docker o directamente en tu sistema.

**Opción 1: Ejecutar con Docker (Recomendado)**

Docker es una forma fácil de hacer que la aplicación funcione sin problemas.

1.  **Consigue el código:**
    Abre la terminal y escribe:
    `git clone [la dirección del proyecto en Github]`
    `cd [el nombre de la carpeta del proyecto]`
    Reemplaza la dirección de Github y el nombre de la carpeta.

2.  **Construye la imagen de Docker:**
    Asegúrate de tener Docker instalado. En la terminal, escribe:
    `docker build -t vulnerabilities-api .`

3.  **Ejecuta la aplicación:**
    Escribe este comando:
    `docker run -p 8000:8000 vulnerabilities-api`

4.  **Accede a la aplicación:**
    Abre tu navegador y ve a:
    `http://localhost:8000/api/`
    (La parte `/api/` podría ser diferente).

**Opción 2: Ejecutar directamente en tu computadora**

Si prefieres no usar Docker, puedes ejecutar la aplicación así:

1.  **Consigue el código:**
    Abre la terminal y escribe:
    `git clone [la dirección del proyecto en Github]`
    `cd [el nombre de la carpeta del proyecto]`
    Reemplaza la dirección de Github y el nombre de la carpeta.

2.  **Crea un "espacio virtual":**
    Escribe esto en la terminal:
    `python -m venv venv`
    Luego, activa el espacio virtual:
    * Linux/Mac: `source venv/bin/activate`
    * Windows: `venv\Scripts\activate`

3.  **Instala las herramientas necesarias:**
    Escribe en la terminal:
    `pip install -r requirements.txt`

4.  **Configura la base de datos:**
    Edita el archivo `vulnerabilities_api/settings.py` con la información de tu base de datos.

5.  **Prepara la base de datos:**
    Ejecuta las migraciones:
    `python manage.py migrate`

6.  **Crea un usuario especial (opcional):**
    Para administrar la aplicación, escribe:
    `python manage.py createsuperuser`

7.  **Ejecuta la aplicación:**
    Escribe en la terminal:
    `python manage.py runserver`

8.  **Accede a la aplicación:**
    Abre tu navegador y ve a:
    `http://127.0.0.1:8000/api/`
    (La parte `/api/` podría ser diferente).
