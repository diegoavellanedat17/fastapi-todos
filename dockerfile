# Python image from the Docker Hub
FROM python:3.9

# Install SQLite3
RUN apt-get update && apt-get install -y sqlite3

# app directory
WORKDIR /app

COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Run the script to initialize the database
RUN chmod +x init_db.sh
RUN ./init_db.sh

# Run the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]