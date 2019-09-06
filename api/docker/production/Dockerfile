# Multi-stage python build ref:
# https://pythonspeed.com/articles/multi-stage-docker-python/
# Not using the virtualenv option as that installs a separate python,
# using the pip install --user option
FROM "tiangolo/uvicorn-gunicorn-fastapi:python3.6-alpine3.8" AS CompileStep

# These packages aren't needed for running production, but we need them to
# compile the python modules we do need.
#
# build-base - for compiling python modules installed by pip
# libffi-dev - for compiling python cryptographic modules
# postgresql-dev - for building psycopg2, python postgres adapter
RUN apk add build-base libffi-dev postgresql-dev

COPY requirements/base.txt base.txt
# we compile the python modules to one place so we can copy it over to the
# final image, this reduces our final image size since we won't bring in
# compilation tools
RUN pip install --user -r base.txt


# The final image we'll run
FROM "tiangolo/uvicorn-gunicorn-fastapi:python3.6-alpine3.8"

# required libs
RUN apk add --no-cache postgresql-libs

# copy over compiled modules
COPY --from=CompileStep /root/.local /root/.local

WORKDIR /app
COPY . /app/
COPY docker/production/prestart.sh prestart.sh
# activate the virtualenv for gunicorn
COPY docker/production/gunicorn_conf.py gunicorn_conf.py
# activate the virtualenv for sh
ENV PATH="/root/.local/bin:$PATH"
