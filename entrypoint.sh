#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

# Set environment variables for the superuser creation
export DJANGO_SUPERUSER_PASSWORD=$SUPER_USER_PASSWORD
export DJANGO_SUPERUSER_NAME=$SUPER_USER_NAME
export DJANGO_SUPERUSER_EMAIL=$SUPER_USER_EMAIL

# Create superuser without interactive input
python manage.py createsuperuser --username $DJANGO_SUPERUSER_NAME --email $DJANGO_SUPERUSER_EMAIL --no-input

# Start gunicorn
gunicorn djang_website.wsgi:application --bind 0.0.0.0:8000
