FROM "tiangolo/uvicorn-gunicorn-fastapi:python3.6-alpine3.8"

# TODO: These packages aren't needed for production, should copy the built python
# modules to a new container in a multistage build and ditch them.
#
# bash - nice to have for when we access the shell in the container
# build-base - for compiling python modules installed by pip
# libffi-dev - for compiling python cryptographic modules
# postgresql-dev - for building psycopg2, python postgres adapter
RUN apk add --no-cache bash build-base libffi-dev postgresql-dev

WORKDIR /app

COPY . /app/ 

# TODO: pip-tools is specified in requirements, but isn't necessary in production,
# consider removing them when building the production image.
RUN pip install -r requirements.txt
