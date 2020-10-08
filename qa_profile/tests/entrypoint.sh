#!/bin/sh

echo "Waiting for app..."

while ! nc -z $APP_HOST $APP_PORT; do
    sleep 0.1
done
echo "app started"


exec "$@"