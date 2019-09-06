#! /usr/bin/env sh

# For the Docker image, this script is executed before the server is
# started.

# fail out on any error
set -e

# Setup the database
echo "Migrating database schema"
alembic upgrade head
