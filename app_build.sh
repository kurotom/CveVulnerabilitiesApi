#!/bin/bash

set -e

echo "Python - collect static files"
python manage.py collectstatic --noinput

echo "Python - making migrations"
python manage.py makemigrations

echo "Python - migrate data"
python manage.py migrate

exec "$@"
