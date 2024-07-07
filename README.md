# FastAPI To Do

Esta corresponde al BE de una aplicación simple de gestión de tareas, registro y autenticación de usuarios

## Instalación

### Prerequisitos

Asegurate que tengas docker instalado en la maquina de destino .[Web oficial de docker](https://www.docker.com/products/docker-desktop).

### Coonfiguración

1. **Clone the repository**:

   ```sh
   git clone https://github.com/yourusername/fastapi-hello-world.git
   cd fastapi-to-dos

   ```

2. **Docker Build and Run**:

   ```sh
   docker build -t fastapi-to-dos .

   docker run -p 8000:8000 fastapi-to-dos
   ```

3. **Access the DB of the dockerContainer**
   ```sh
   docker ps
   docker exec -it <container-id> /bin/bash
   sqlite3 todos.db
   ```
