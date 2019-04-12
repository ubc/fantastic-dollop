# Web Component

This is a web skeleton with a basic user login functionality.

## Setup (Non-Docker)

Consult the `README.md` in the API and UI subdirectories.

## Setup (Docker)

Note that the docker setup is configured for development by default. Traffic is served over unencrypted http. Production setups should, at a minimum, use encrypted https.

#### Docker Prerequisites

The `docker` and `docker-compose` commands must be available. If you're using older versions than specified, it might still work, it's just untested.

* [Docker](https://docs.docker.com/install/), at least v18.06
* [Docker Compose](https://docs.docker.com/compose/install/), at least 1.17

#### Run

Make sure you're in the web component's root directory (where this README is located) and run:

    docker-compose up

* The UI should be accessible at [http://localhost:5000/](http://localhost:5000/).
* The API should be accessible at [http://localhost:5001/](http://localhost:5001/).

Changes to the source files should automatically be reflected to the running containers. In practice, frontend CSS sometimes don't go through properly, so you might need to manually refresh the page to see the changes.

The default `docker-compose up` command will start the containers in the foreground, showing all log output directly. To exit, press `Ctrl`-`c` or whatever key combo your OS uses to send SIGINT.

##### Execute Commands

To run arbitary commands, just replace `<COMMAND>` with what you wish to run:

    docker-compose exec <SERVICENAME> <COMMAND>

Check `docker-compose.yml` for the service names you should use in place of `<SERVICENAME>`.

Example:

* To get shell access in the UI container, just execute `bash`

        docker-compose exec ui bash

###### Hard Reset

**WARNING:** This will remove all data and containers!

    docker-compose down -v


###### Running in the Background

If you wish to run this in the background, without the live log output, add the `-d` option:

    docker-compose up -d

To stop running:

    docker-compose stop


To access the logs in this mode, run: 

    docker-compose logs <SERVICENAME>

Examples:

* API  

        docker-compose logs api

* API's Database (Postgre)

        docker-compose logs api_db

