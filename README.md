# Introducción

El repositorio consiste del desarrollo del Test Práctico para la postulación al cargo de Developer en CHR.
Para este, se tuvieron que resolver dos tareas ocupando el framework Django:

(1) Acceder a los datos desde la API [Bike Santiago](http://api.citybik.es/v2/networks/bikesantiago), crear un modelo para guardar los datos obtenidos.
De manera opcional, se pedía que estos se visualizaran a través de una vista, así como también en el panel de administrador.

(2) Acceder a los datos de proyectos de publicados en la página del [Servicio de Evaluación Ambiental](https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php),
los que debían ser descargados y sistematizados a tarvés del uso de alguna librería de _web scrapping_, y posteriormente crear un modelo para guardarlos. Finalmente,
se debía integrar que estos se guardaran en formato JSON. De manera opcional, se pedía que estos se visualizaran a través de una vista,
así como también en el panel de administrador.

# Dependencias

Para el desarrollo del proyecto se ocupó el framework [Django](https://www.djangoproject.com/), así como librerías de _web scrapping_ y análisis y manejo de datos.
La lista completa de ellas se encuentra en el archivo ``requirements.txt``

# Ejecución del proyecto

Se recomienda instalar las librerías en un entorno virtual, para lo cual se deben seguir los siguientes pasos:

```
git clone url
cd dir
python -m venv venv
source venv/Scripts/Activate
pip install requirements.txt
```

Nota: El proyecto está configurado para conectarse a una base de datos PostgreSQL llamada `chr_db`, por lo que previamente [PostgreSQL](https://www.postgresql.org/) debe
ser instalado y la base de datos creada en `pgAdmin4` ocupando la contraseña `1234` de acuerdo a lo configurado en el archivo `/test_chr/.env`.

Para consultar la instalación de este se recomienda [revisar la siguiente guía](https://medium.com/star-gazers/data-workflow-with-django-pandas-postgresql-and-docker-56fbf2bc1105).

Para ejecutar el servidor se deberá activar a través de los comandos

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

y finalmente abrir la dirección [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

# Navegación

Desde el _home_ se puede acceder a las distintas partes del proyecto, a través de los links presentes en la barra de navegación.

# Tarea 1.- Bike Santiago

Inicialmente, al abrir la pestaña _Bike Santiago_ no se visualizarán registros, los que en primera instancia deben ser descargados. Para ello, ocupar el botón de "Cargar estaciones".
Al hacerlo, se generará una entidad del modelo para cada una de las estaciones obtenidas a través de la API. Para obtener estas se ocupó la descarga de elementos a través de la librería `requests`, y posteriormente fueron procesados en `pandas` para adaptar la información a los formatos de datos correctos.

La información obtenida es visualizada en formato de _tarjeta_, y se mantiene fija en la base de datos hasta el momento en que se quiera actualizar la lista de estaciones, para lo cual se generó el botón _Actualizar estaciones_. Con el fin de evitar duplicados, cada actualización elimina las entidades existentes para volver a generarlas. Se identifica como un aspecto a mejorar en una futura iteración del proyecto el solo eliminar aquellas estaciones que hayan sido actualizadas desde la última actualización.

# Tarea 2.- Servicio de Evaluación Ambiental

Inicialmente, al abrir la pestaña _SEIA_ no se visualizarán registros, los que en primera instancia deben ser descargados. Para ello, ocupar el botón de "Cargar proyectos".
Al hacerlo, se generará una entidad del modelo para cada uno de los proyectos obtenidos mediante _web scrapping_. Para obtener estos se ocuparon las librerías `requests y BeautifulSoup`, y posteriormente fueron procesados en `pandas` para adaptar la información a los formatos de datos correctos.

La información obtenida es visualizada en formato de tabla. Al igual que con _Bike Santiago_, esta se mantiene fija en la base de datos hasta el momento en que se quiera actualizar la lista de proyectos, donde se eliminan los registros con el fin de evitar duplicados al generar nuevos, por lo que en una futura iteración se podría mejorar a través de identificar solo los nuevos elementos.

Notas:

- Para la prueba del proyecto se limitó a una búsqueda por 10 páginas de un total de 28.446 existentes al momento de la realización de este. Para modificar el código y permitir que este itere sober la totalidad de las páginas, en el archivo `seia/models.py` se descomentar la línea 26 y comentar la línea 27

```
[26] # for i, _ in enumerate(iter(bool, True), start=1): # Busca valores hasta el infinito
[27] for i in range(1, 11):
```

- El archivo JSON se guarda de manera local en la carpeta del proyecto, en la ubicación `seia/json/exportado.json`

# Panel de administrador

Todas las entidades generadas pueden ser visualizadas y modificadas en el panel de administrador, al cual se puede acceder a través de la barra de navegación. Para ingresar a él se dejó de manera preconfigurada una cuenta de *superuser* con los datos:

```
user: chr
password: 1234
```
