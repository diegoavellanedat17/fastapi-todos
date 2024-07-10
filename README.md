# FastAPI To Do
## Ingresa al siguiente link para ver la aplicaión web en funcionamiento 🚀 [Mis Tareas](http://54.152.5.128:3000/)

Esta corresponde al BE de una aplicación simple de gestión de tareas, registro y autenticación de usuarios

## Instalación

### Prerequisitos

Asegúrate de tener Docker instalado en la máquina de destino (si quieres correrlo con Docker). [Web oficial de Docker](https://www.docker.com/products/docker-desktop).

### Configuración

1. **Clone the repository**:

   ```sh
   git clone https://github.com/diegoavellanedat17/fastapi-hello-world.git
   cd fastapi-to-dos
   ```
   
2. **Genera la clave secreta para JWT**:

   ```sh
   openssl rand -base64 32
   ```
   Crea un archivo .env en la raíz de la carpeta y guarda la clave secreta generada:

   ```sh
   SECRET_KEY=26kVSvW6+njzlj5SUPxXmHYiqAVsD/kFQn9soumBxsk=
   ```
3. **Docker Build y Run**:

   ```sh
   docker build -t fastapi-to-dos .
   docker run -d -p 8000:8000 fastapi-to-dos
   ```
   Acceso a la base de datos del contenedor Docker:
   
   ```sh
   docker ps
   docker exec -it <container-id> /bin/bash
   sqlite3 todos.db
   ```

## Ejecución Local
Para ejecutar localmente con Docker:

1. Clona el repositorio y configura la clave secreta como se menciona arriba.
2. Construye la imagen Docker y ejecútala con los comandos proporcionados.

Para ejecutar localmente sin Docker:

1. Clona el repositorio y configura la clave secreta como se menciona arriba.
2. Instala las dependencias de Python especificadas en requirements.txt.
3. Ejecuta la aplicación usando el comando adecuado para tu entorno.

## Colección de Postman
La colección de Postman para este proyecto está disponible en el archivo Fast API TO DOs.postman_collection. Puedes importarla en Postman siguiendo estos pasos:

1. Abre Postman.
2. Haz clic en "Import" en la esquina superior izquierda.
3. Selecciona el archivo Fast API TO DOs.postman_collection.
4. Haz clic en "Import" para agregar la colección a tu Postman.
5. Esta colección incluye todas las rutas necesarias para interactuar con la API.
   
## Descripción
Esta colección incluye todas las rutas necesarias para interactuar con la API. A continuación, se describen las principales rutas y sus métodos:

## Descripción de las Funcionalidades

### Crear una nueva tarea

- **Descripción:** Permite crear una nueva tarea.
- **Método:** POST
- **Endpoint:** `/tasks/`
- **Body:** Debe incluir los datos de la tarea a crear.
- **Headers:** Se requiere un token de autenticación válido.

### Obtener todas las tareas

- **Descripción:** Obtiene todas las tareas creadas por el usuario autenticado.
- **Método:** GET
- **Endpoint:** `/tasks/`
- **Headers:** Se requiere un token de autenticación válido.

### Obtener una tarea específica por ID

- **Descripción:** Obtiene detalles de una tarea específica por su ID.
- **Método:** GET
- **Endpoint:** `/tasks/{task_id}`
- **Parámetros de ruta:** `task_id` - ID de la tarea a consultar.
- **Headers:** Se requiere un token de autenticación válido.

### Actualizar una tarea existente por ID

- **Descripción:** Actualiza los detalles de una tarea existente por su ID.
- **Método:** PUT
- **Endpoint:** `/tasks/{task_id}`
- **Parámetros de ruta:** `task_id` - ID de la tarea a actualizar.
- **Body:** Debe incluir los datos actualizados de la tarea.
- **Headers:** Se requiere un token de autenticación válido.

### Eliminar una tarea por ID

- **Descripción:** Elimina una tarea específica por su ID.
- **Método:** DELETE
- **Endpoint:** `/tasks/{task_id}`
- **Parámetros de ruta:** `task_id` - ID de la tarea a eliminar.
- **Headers:** Se requiere un token de autenticación válido.

## Ejecutar tests con Docker
``` sh
docker exec -it <container-id> pytest
```

## Ejecutar tests sin Docker
```sh
pytest
```
Asegúrate de tener un entorno configurado adecuadamente antes de ejecutar los tests. Los tests deben ejecutarse sin errores para verificar el correcto funcionamiento de la aplicación.
