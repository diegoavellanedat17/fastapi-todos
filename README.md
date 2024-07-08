# FastAPI To Do

Esta corresponde al BE de una aplicación simple de gestión de tareas, registro y autenticación de usuarios

## Instalación

### Prerequisitos

Asegurate que tengas docker instalado en la maquina de destino .[Web oficial de docker](https://www.docker.com/products/docker-desktop).

### Coonfiguración

1. **Clone the repository**:

   ```sh
   git clone https://github.com/diegoavellanedat17/fastapi-hello-world.git
   cd fastapi-to-dos

   ```

2. **Generate the SecretKey for the JWT**:

   ```sh
   openssl rand -base64 32
   ```

   Create a file .env in the root of the folder and save as:
   SECRET_KEY=26kVSvW6+njzlj5SUPxXmHYiqAVsD/kFQn9soumBxsk=

3. **Docker Build and Run**:

   ```sh
   docker build -t fastapi-to-dos .

   docker run -p 8000:8000 fastapi-to-dos
   ```

4. **Access the DB of the dockerContainer**
   ```sh
   docker ps
   docker exec -it <container-id> /bin/bash
   sqlite3 todos.db
   ```

## Postman Collection

La colección de Postman para este proyecto está disponible en el archivo `Fast API TO DOs.postman_collection`. Puedes importarla en Postman siguiendo estos pasos:

1.  Abre Postman.
2.  Haz clic en "Import" en la esquina superior izquierda.
3.  Selecciona el archivo `Fast API TO DOs.postman_collection`.
4.  Haz clic en "Import" para agregar la colección a tu Postman.

Esta colección incluye todas las rutas necesarias para interactuar con la API.
