#!/bin/sh

if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    python manage.py createsuperuser --no-input
fi

gunicorn shopsmart.wsgi --user nginx --bind 0.0.0.0:8000 --workers 3 &
nginx -g "daemon off;"