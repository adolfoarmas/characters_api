# Characters API🤖

API para obtener, crear y eliminar caracteres construida con FastAPI.

El repositorio cuenta con una base de datos sqlite3, previamente migrada y a la cual se le han incluido datos de prueba.

A continuación, pasos para desplegar la aplicación utilizando Docker.

## Requisitos

- Docker

## Estructura del Proyecto

- `main.py`: Archivo principal de la aplicación FastAPI.
- **`src/`: Base de codigo relativa al proyecto.**

  - `api/`: Configuracion de versionado de API, rutas, esquemas de validación y excepciones.
  - `core/`: Configuración de sesion(es) de base de datos y seeds.
  - `domain/`: Modelos
  - `infrastructure/`: Manejo de querys (CRUD) a la BD.
  - `use_cases`: Manejo de logica de negocio.
- `tests/`: Configuracion de pruebas unitarias.
- `alembic/`: Carpeta de alembic para manejo y almacenamiento historico de migraciones de la BD.
- `postman/`: Contiene colección de [Postman](https://www.postman.com/downloads/) para pruebas desde dicha aplicación.
- `Dockerfile`: Archivo de configuración para crear la imagen de Docker.
- `requirements.txt`: Archivo que contiene las dependencias del proyecto.
- `api.db`: Base de datos SQLite
- `alembic.ini`: Archivo de configuración de alembic.

## Despliegue con Docker

### 1. **Clonar el repositorio**

```bash
   git clone characters_api
   cd characters_api
```

### 2. **Construir la imagen de Docker**

```
docker build -t characters-api .
```

### 3. **Ejecutar el contenedor**

```
docker run -d -p 8000:80 characters-api
```

Se ejecuta el contenedor de la aplicación y se envia la informacion desde el puerto 80 del mismo al puerto 8000 del docker host.

### 4. **Acceder a la documentación de la API:**

Desde un navegador abrir http://localhost:8000/docs para ver la documentación de la API.
