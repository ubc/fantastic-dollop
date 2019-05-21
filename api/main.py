import logging
import logging.config
import os
import yaml # for reading the logging config file

from fastapi import FastAPI
from app.controllers import users
from app.controllers import signin
from app import db

# Configures logging for the whole app, will default to using the settings
# in `config/logging.yml` which will set logging at DEBUG to stdout. The config
# file path can be overridden with the environment variable `LOG_CONFIG`.
configPath = "config/logging.yml"
envConfigPath = os.getenv("LOG_CONFIG", None)
if envConfigPath:
    configPath = envConfigPath
if os.path.exists(configPath):
    with open(configPath, 'rt') as f:
        config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
else:
    logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger(__name__)

app = FastAPI()

app.include_router(users.router)
app.include_router(signin.router)

@app.get("/")
async def root():
    log.debug("HELLO WORLD 1")
    return {"message": "Hello World"}

@app.get("/items/")
async def read_items():
    log.debug("HELLO WORLD")
    return "blah"

@app.on_event("startup")
async def startup():
    await db.connect()

@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()
