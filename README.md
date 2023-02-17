# Test Developer

_Proyecto a modo de test de habilidades prácticas en opción de la plaza de Back-End Developer_

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Despliegue** para conocer como desplegar el proyecto.

### Pre-requisitos 📋

Primeramente se necesita tener el códiog fuente en el ordenador local, para ello usando la herramienta de git en su sistema operativo puede utilizar
```
git clone https://github.com/amian98/test_developer.git
```
Además del código fuente, necesitará herramientas para configurar las librerías de su sistema operativo, y para ello se creará un entorno virtual que 
permita mantener coherentes las versiones del _software_. Primeramente, instalamos y actualizamos _pip_
```
python3 -m pip install --upgrade pip
```

Y al concluir procedemos al mismo paso para _virtualenv_, paquete de _python3_ que nos permitirá crear el entorno aislado donde existirá nuestra aplicación
de _Django_
```
pip3 install virtualenv
```
Con estas librerias instaladas y actualizadas podemos crear el entorno virutal
```
python3 -m venv test-env
```
Y activarlo en el terminal 
```
source text-env/bin/activate
```
Una vez con el entorno virtual activo en el terminal, deberá instalar las dependencias que fueron utilizadas para desarrollar las aplicaciones del 
proyecto de _Django_. Para ello en el directorio raíz del proyecto encontrará un fichero `requirements.txt` que mediante la linea

```
python -m pip install -r requirements.txt
```
Dejará su entorno virtual con las versiones requeridas por el proyecto de _Django_.

### PostgreSQL
Para poder ejecutar el código se necesitará de una base de datos _Postgre_ configurada en el proyecto; para alejar esta configuración mandatoria del
desarrollo del proyecto, se creó el fichero `test_developer/.env` con la configuración que requiere _Django_. O bien debe modificar este fichero con 
configuración de la base de datos y el rol que utilizará para desplegar la aplicación, o deberá crear la base de datos y el rol que se especifican el
fichero de configuración de la base de datos.

## Despliegue 📦
Primeramente se requiere crear la base de datos con las tablas programadas en los modelos para el funcionamiento de la aplicación, para ello antes de
desplegar el sitio utilizaremos el `manage.py` para crear las tablas en _PostgreSQL_ mediante los comandos

```
python manage.py makemigrations
python manage.py migrate
```
Para el llenado de la base de datos se requiere correr otros tres comandos, para su explicación ver **Herramientas**.
```
python manage.py updatebike
python manage.py scrap
python manage.py updateregister
```
Una vez las tablas creadas y con el propósito de comprobar el funcionamiento del _software_ y el cumplimiento de las tareas asignadas, desplegará 
_Django_ sobre su servidor de prueba mediante el comando

```
python manage.py runserver
```
Quedando por defecto accesibe desde su `localhost`.

## Navegación
En la aplicación son accesibles tres URLs, [el sitio de administración](http://localhost:8000/admin), al que puede acceder usando como creedenciales 
`user:admin` `pass:admin` teniendo completo control sobre todos los modelos utilizados para describir los datos que se almacenan en el sistema. Las otras
dos URLs pertenecen a tablas paginadas para mostrar los datos de cada uno de los ejercicios asignados. Las tablas fueron renderizadas desde 
_Django-Template_ con estilo de _bootstrap5_ y hasta este punto permiten visualizar si bien todas las entradas de la base de datos, solo permite los campos
con más sentido, la vista detallada solo es accesible desde la administración. 

A las vistas tabuladas del [Servicio de Evaluación Ambiental](http://localhost:8000/seia) y de
[Bike Santiago](http://localhost:8000/bike) es posible acceder sin autenticación.

## Herramientas :hammer:

Para el cumplimiento de la encomienda se programaron tres comandos para el `manage.py` que permitieran agregarle al proyecto las principales
caracteristicas del test:

-`updatebike`: Utilizando la librería `requests` de python realiza peticiones a la API designada para ello, e inyecta en la base de datos la 
información que obtine de esa consulta.

-`scrap`: Mediante el paquete BeautifullSoup4 _scrappea_ el sitio correspondiente realizando peticiones sucesivas con los debidos parámetros,
permitiendo obtener la totalidad de la tabla de interés, exportando esta información a formato `JSON`.

-`updateregister`: carga el fichero `JSON` exportado por el comando anteriormente expuesto, e inserta esa información en la base de datos.
