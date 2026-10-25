# Small official Python image
FROM python:3.11-slim

# Folder inside the container where our code will live
WORKDIR /app

# Copy requirements first so Docker can cache the install step
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Turn off Flask debug mode inside the container
ENV FLASK_DEBUG=0

# Flask listens on port 5000
EXPOSE 5000

# Start the app
CMD ["python", "app.py"]
