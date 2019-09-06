#! /usr/bin/env sh

# For the Docker image, this script is executed before the server is
# started.
# This is the development prestart, production prestart is located in
# docker/production/prestart.sh

# fail out on any error
set -e

# Development Only, update dependencies
echo "Update dependencies using pip-sync"
pip-sync requirements/test.txt

# Setup the database
echo "Migrating database schema"
alembic upgrade head
