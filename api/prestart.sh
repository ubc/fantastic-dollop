#! /usr/bin/env sh

# For the Docker image, this script is executed before the server is
# started. Update the dependencies in case the user has added any.
#
# NOTE: Only necessary in development where dependencies might change.

set -e

echo "Update dependencies using pip-sync"
pip-sync

