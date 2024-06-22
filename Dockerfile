# Use a standard Linux distribution base image for better compatibility
FROM python:3.8-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    libblas-dev \
    liblapack-dev \
    gfortran \
    libpq-dev \
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

# Start script or command
COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]

EXPOSE 8000