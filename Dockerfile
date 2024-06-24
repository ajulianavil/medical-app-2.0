# Use a standard Linux distribution base image for better compatibility
FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    libblas-dev \
    liblapack-dev \
    gfortran \
    libpq-dev \
    dos2unix \
    && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy and install requirements
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

# Copy project files
COPY . /app

# Ensure the entrypoint script is executable and convert line endings
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh && dos2unix /entrypoint.sh

# Start script or command
ENTRYPOINT ["sh", "/entrypoint.sh"]

EXPOSE 8000
