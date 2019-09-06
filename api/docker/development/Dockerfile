FROM "tiangolo/uvicorn-gunicorn-fastapi:python3.6-alpine3.8"

# bash - nice to have for when we access the shell in the container
# build-base - for compiling python modules installed by pip
# libffi-dev - for compiling python cryptographic modules
# postgresql-dev - for building psycopg2, python postgres adapter
RUN apk add --no-cache bash build-base libffi-dev postgresql-dev

WORKDIR /app

COPY . /app/

RUN pip install -r requirements/development.txt
