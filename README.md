# Introducción

El repositorio consiste del desarrollo del Test Práctico para la postulación a CHR.
Para este, se tuvieron que resolver dos tareas ocupando el framework Django:

(1) Acceder a los datos desde la API [Bike Santiago](http://api.citybik.es/v2/networks/bikesantiago), crear un modelo para guardar los datos obtenidos.
De manera opcional, se pedía que estos se visualizaran a través de una vista, así como también en el panel de administrador.

(2) Acceder a los datos de proyectos de publicados en la página del [Servicio de Evaluación Ambiental](https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php), 
los que debían ser descargados y sistematizados a tarvés del uso de alguna librería de *web scrapping*, y posteriormente crear un modelo para guardarlos. Finalmente, 
se debía integrar que estos se guardaran en formato JSON. De manera opcional, se pedía que estos se visualizaran a través de una vista, 
así como también en el panel de administrador.

# Dependencias

Para el desarrollo del proyecto se ocupó el framework Django, así como librerías de *web scrapping* y análisis y manejo de datos.
La lista completa de ellas se encuentra en el archivo requirements.txt

# Ejecución del proyecto

Se recomienda instalar las librerías en un entorno virtual, para lo cual se deben seguir los siguientes pasos:

```
git clone url
cd dir
python -m venv venv
source venv/Scripts/Activate
pip install requirements.txt
```

Nota: El proyecto está configurado para conectarse a una base de datos PostgreSQL llamada ``chr_db``, por lo que previamente [PostgreSQL](https://www.postgresql.org/) debe
ser instalado y la base de datos creada en ``pgAdmin4`` ocupando la contraseña ``1234`` de acuerdo a lo configurado en el archivo ``/test_chr/.env``

Para ejecutar el servidor se deberá activar a través de los comandos

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

y finalmente abrir la dirección [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

# Partes del proyecto

